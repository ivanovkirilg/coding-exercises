## Exercises from [TDD Manifesto](https://tddmanifesto.com/exercises/)

- The page suggests to first read
  [Getting started](https://tddmanifesto.com/getting-started/)
  and [A clean test](https://tddmanifesto.com/a-clean-test/).
- Try not to read ahead of the being solved exercise.
- Solve only one requirement at a time.

### Key takeaways from *Getting started*

#### Three laws of TDD
1. You are not allowed to write any production code
   unless it is to make a failing unit test pass.
2. You are not allowed to write any more of a unit test
   than is sufficient to fail, and compilation failures are failures.
3. You are not allowed to write any more production code
   than is sufficient to pass the one failing unit test.

#### Red-Green-Refactor cycle
- <red> Write a failing test. </red>
  Base it on a specific requirement. Follow law 2.
- <green> Make the test pass. </green>
  Write production code only sufficient to make the test pass (law 3).
- <blue> Refactor. </blue>
  Never refactor in other phases, only here.

<img src="https://tddmanifesto.com/wp-content/uploads/2021/05/tddcycle-1024x683.png"
     alt="Fail > Pass > Refactor"
     width="400">

#### Key takeaways from *A clean test*
Clean code requires clean tests.
Write all parts of the software with equal care (production or test code).

A clean test reads like a story.
A clean test should contain all the information necessary to understand what is being tested.

#### Characteristics of a clean test
- Descriptive test name
  - Consider patterns GivenWhenThen & ShouldWhen
- Meaningful namings
- Structured with the Arrange-Act-Assert (AAA) pattern
- Follows the F.I.R.S.T principle
  - Fast
  - Independent
  - Repeatable
  - Self-validating
  - Thorough
- Asserts one behavior
- Uses meaningful test data
  - Tests are examples of code usages.
    They are executable documentation for the use cases.
- Hide irrelevant data for the test
  - Use test data builders

#### Example
Instead of this:

<img src="https://tddmanifesto.com/wp-content/uploads/2021/07/TDD-example-noncleancode-1200x454.png"
     alt="Non-clean test example"
     width="600">

Write this:

<img src="https://tddmanifesto.com/wp-content/uploads/2021/07/TDD-example-cleancode-1200x447.png"
     alt="Clean test example"
     width="600">



<style>
red {
    color: #f00
}
green {
    color: #3b3
}
blue {
    color: #36f
}
</style>
