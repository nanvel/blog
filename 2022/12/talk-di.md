labels: Talk
        Ruby
        SoftwareDevelopment
        SoftwareDesign
created: 2022-12-03T11:10
modified: 2022-12-03T11:10
place: Bangkok, Thailand
comments: false

# Dependency Injection with Dry::Container

[Github](https://github.com/nanvel/slides-di)

<object data="slides-di.pdf" type="application/pdf" width="800px" height="600px">
    <embed src="slides-di.pdf">
        <p>This browser does not support PDFs. Please download the PDF to view it: <a href="slides-di.pdf">Download PDF</a>.</p>
    </embed>
</object>

Todo app example:
```ruby
require 'dry/container'


module Models
  class Task
    attr_reader :id
    attr_accessor :text, :priority

    def initialize(id:, text:, priority:)
      @id = id
      @text = text
      @priority = priority
    end
  end
  
  class Priority
    attr_reader :value
    
    LOW = 0
    MEDIUM = 1
    HIGH = 2

    ALL = [LOW, MEDIUM, HIGH]

    def initialize(value)
      raise "Invalid priority value." unless ALL.include?(value)
      @value = value
    end
    
    def max?
      @value == HIGH
    end

    def min?
      @value == LOW
    end

    def up
      return self if max?

      self.class.new(@value + 1)
    end

    def down
      return self if min?

      self.class.new(@value - 1)
    end

    def self.low
      self.new LOW
    end
  end
end


module Factories
  class Task
    def initialize(enumerator:)
      @enumerator = enumerator
    end

    def call(text:, priority:)
      task_id = @enumerator.next

      Models::Task.new(
        id: task_id,
        text: text,
        priority: priority,
      )
    end
  end
end


module Repositories
  class Tasks
    def initialize
      @tasks = []
    end

    # commands

    def add(task)
      @tasks.push(task)
    end
      
    def remove_by_id(task_id)
      @tasks = @tasks.select { |task| task.id != task_id }
    end

    # queries

    def list
      @tasks.sort_by { |task| task.priority.value }.reverse
    end

    def find_by_id(task_id)
      @tasks.detect { |task| task.id == task_id }
    end
  end
end


module TaskPrinters
  class Base        
    def call(task)
      raise NotImplementedError, 'Provide implementation for #call'
    end
  end

  class Plain < Base
    def call(task)
      "- #{task.id}: #{task.text}"
    end
  end
  
  class Csv < Base
    def call(task)
      "#{task.id},#{task.text},#{task.priority.value}"
    end
  end
end


module UseCases
  class PrintTasks
    def initialize(task_printer:, tasks_repository:)
      @task_printer = task_printer
      @tasks_repository = tasks_repository
    end
    
    def call
      @tasks_repository.list.each do |task|
        output = @task_printer.call(task)

        puts output
      end
    end
  end

  class AddTask
    def initialize(task_factory:, tasks_repository:)
      @task_factory = task_factory
      @tasks_repository = tasks_repository
    end
    
    def call(text)
      task = @task_factory.call(
        text: text,
        priority: Models::Priority.low
      )

      @tasks_repository.add(task)
    end
  end
  
  class RemoveTask
    def initialize(tasks_repository:)
      @tasks_repository = tasks_repository
    end

    def call(task_id)
      @tasks_repository.remove_by_id(task_id)
    end
  end

  class EditTask
    def initialize(tasks_repository:)
      @tasks_repository = tasks_repository
    end

    def call(task_id:, text:)
      task = @tasks_repository.find_by_id(task_id)
      return if task.nil?

      task.text = text
    end
  end

  class UpTask
    def initialize(tasks_repository:)
      @tasks_repository = tasks_repository
    end

    def call(task_id:)
      task = @tasks_repository.find_by_id(task_id)
      return if task.nil?

      task.priority = task.priority.up
    end
  end

  class DownTask
    def initialize(tasks_repository:)
      @tasks_repository = tasks_repository
    end

    def call(task_id:)
      task = @tasks_repository.find_by_id(task_id)
      return if task.nil?

      task.priority = task.priority.down
    end
  end
end


module Container
  def self.build
    container = Dry::Container.new

    container.namespace('todo') do
      register(:task_enumerator, memoize: true) do
        (0..Float::INFINITY).to_enum
      end

      register(:task_factory, memoize: true) do
        Factories::Task.new(
          enumerator: resolve(:task_enumerator),
        )
      end

      register(:tasks_repository, memoize: true) do
        Repositories::Tasks.new
      end

      register(:plain_printer, memoize: true) do
        TaskPrinters::Plain.new
      end

      register(:csv_printer, memoize: true) do
        TaskPrinters::Csv.new
      end

      register(:print_tasks) do
        UseCases::PrintTasks.new(
          tasks_repository: resolve(:tasks_repository),
          task_printer: resolve(:plain_printer),
        )
      end

      register(:add_task) do
        UseCases::AddTask.new(
          tasks_repository: resolve(:tasks_repository),
          task_factory: resolve(:task_factory),
        )
      end

      register(:remove_task) do
        UseCases::RemoveTask.new(
          tasks_repository: resolve(:tasks_repository),
        )
      end

      register(:edit_task) do
        UseCases::EditTask.new(
          tasks_repository: resolve(:tasks_repository),
        )
      end

      register(:up_task) do
        UseCases::UpTask.new(
          tasks_repository: resolve(:tasks_repository),
        )
      end

      register(:down_task) do
        UseCases::DownTask.new(
          tasks_repository: resolve(:tasks_repository),
        )
      end
    end
  end
end


if __FILE__ == $0
  container = Container.build

  add_task = container.resolve('todo.add_task')
  print_tasks = container.resolve('todo.print_tasks')
  remove_task = container.resolve('todo.remove_task')
  edit_task = container.resolve('todo.edit_task')
  up_task = container.resolve('todo.up_task')
  down_task = container.resolve('todo.down_task')

  puts 'Create 2 tasks:'

  add_task.call('A task example!')
  add_task.call('Another task!')
  up_task.call(task_id: 0)
  print_tasks.call

  puts 'Edit task:'

  edit_task.call(task_id: 1, text: 'Text updated!')
  print_tasks.call

  puts 'Increase priority:'

  up_task.call(task_id: 1)
  print_tasks.call

  puts 'Remove a task:'

  remove_task.call(0)
  print_tasks.call
end
```

Tests example:
```ruby
require 'dry/container/stub'
require 'rspec'

require './main'


RSpec.describe Repositories::Tasks do
  it 'is empty initially' do
    expect(subject.list).to be_empty
  end

  context 'with tasks' do
    let(:priority0) { double('priority0', value: Models::Priority::HIGH) }
    let(:priority1) { double('priority1', value: Models::Priority::MEDIUM) }
    let(:task0) { double('task0', id: 0, priority: priority0) }
    let(:task1) { double('task1', id: 1, priority: priority1) }

    before do
      subject.add(task0)
      subject.add(task1)
    end

    describe '#list' do
      it 'returns all tasks' do
        expect(subject.list).to eq([task0, task1])
      end
    end

    describe '#find_by_id' do
      it 'returns task for the specified id' do
        expect(subject.find_by_id(task0.id)).to eq(task0)
      end

      it 'returns nil if not found' do
        expect(subject.find_by_id(2)).to be_nil
      end
    end

    describe '#remove_by_id' do
      it 'removes task with specified id' do
        expect { subject.remove_by_id(task0.id) }
          .to change { subject.list.size }.by(-1)
      end

      it 'does not remove if not found' do
        expect { subject.remove_by_id(2) }
          .not_to change { subject.list.size }
      end
    end
  end
end


RSpec.describe UseCases::AddTask do
  let(:enumerator) { double('enumerator', next: 1) }
  let(:task_factory) { Factories::Task.new(enumerator: enumerator) }
  let(:tasks_repository)  { double('tasks_repository', add: nil) }
  let(:text) { 'Test text' }

  subject do
    described_class.new(
      task_factory: task_factory,
      tasks_repository: tasks_repository,
    )
  end

  it 'adds task to the repository' do
    subject.call(text)

    expect(tasks_repository).to have_received(:add).with(Models::Task) do |task|
      expect(task.priority.min?).to be_truthy
      expect(task.text).to eq(text)
    end
  end
end


RSpec.describe 'A container test' do
  let(:task) do
    Models::Task.new(
      id: 1,
      text: 'Example text.',
      priority: Models::Priority.low
    )
  end
  let(:tasks_repository) do
    double('tasks_repository', add: nil, list: [task])
  end

  subject { Container.build }

  before do
    subject.enable_stubs!
    subject.stub('todo.tasks_repository', tasks_repository)
  end

  it 'prints added task' do
    print_tasks = subject.resolve('todo.print_tasks')

    expect { print_tasks.call }.to output("- 1: Example text.\n").to_stdout
  end
end
```
