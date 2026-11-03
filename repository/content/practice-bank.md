# Software and Symbolic AI practice bank

Team DLLM • Study edition • 3 November 2026

## How to practise

20 true/false, 20 single-answer multiple-choice, and 6 extended questions. Section numbers refer to the two-chapter guide. These are practice questions, not official exam questions.

**Start small:** Try TF01–TF08 and MC01–MC08 after Software. Then try the remaining objective items after Symbolic AI. Mark each answer sure or unsure. Check the key only after your attempt, including answers you guessed correctly.

**Short first session:** Start with TF03, TF07, MC05 and MC07 for software, then TF11, MC12, MC14 and MC18 for symbolic AI. For each mistake, reread its section and retry with the answer covered.

**For extended questions:** Give a developed answer (about 100 words or more) or equivalent labelled reasoning, such as a trace or test table. The key shows a short worked route you can use to check your reasoning.

**Self-check:** For a missed item, write one sentence explaining the error and the section you will reread. The answer key follows all 46 questions.

<!--page-->

## True or false • Part 1

Mark T or F. If false, correct the statement.

**TF01 · §1.1**  A phone screen is hardware.   [   ]

**TF02 · §1.1**  A room-booking application is system software.   [   ]

**TF03 · §1.2**  An output can be a question asking for missing information.   [   ]

**TF04 · §1.3**  An algorithm must be written in Python.   [   ]

**TF05 · §1.4**  “Ask for availability when status is unknown” is a testable requirement.   [   ]

**TF06 · §1.4**  Passing input validation proves the room is really open.   [   ]

**TF07 · §1.5**  Write an expected output before running the test.   [   ]

**TF08 · §1.5**  One successful open-room test proves that the program handles a change to closed.   [   ]

**TF09 · §2.1**  Enrolled(AI101, Mina) means the same thing as Enrolled(Mina, AI101).   [   ]

**TF10 · §2.2**  Inclusive OR is true when both inputs are true.   [   ]

<!--page-->

## True or false • Part 2

Mark T or F. If false, correct the statement.

**TF11 · §2.2**  From IF A THEN B and B alone, A must follow.   [   ]

**TF12 · §2.3**  Forward chaining starts with facts.   [   ]

**TF13 · §2.3**  Backward chaining treats the requested goal as already proved.   [   ]

**TF14 · §2.3**  In Mina’s adviser, missing open establishes closed.   [   ]

**TF15 · §2.4**  The order in which BFS removes states is always a path.   [   ]

**TF16 · §2.4**  With equal action costs, BFS can find a least-cost path by finding a fewest-action path.   [   ]

**TF17 · §2.5**  An action needs all its preconditions before it can run in our model.   [   ]

**TF18 · §2.6**  A learner wanting quiet establishes that Room A is quiet.   [   ]

**TF19 · §2.6**  The inference engine applies rules to the current case facts.   [   ]

**TF20 · §2.7**  A correct rule trace can use an outdated room fact.   [   ]

<!--page-->

## Multiple choice • 1 to 4

Choose one answer per question.

**MC01 · §1.1**  Which item is application software?

A. Physical display

B. Room-booking app

C. Operating system

D. Processor

**MC02 · §1.1**  What is the operating system’s role here?

A. Inspect room noise

B. Book a room

C. Manage hardware resources

D. Supply electricity

**MC03 · §1.2**  Mina enters “I need quiet.” What role does this statement play?

A. Input

B. Processing

C. Output

D. Test result

**MC04 · §1.2**  Which is processing?

A. Mina types a room name

B. The screen displays a question

C. The room status is supplied

D. The program compares the facts with its rules

<!--page-->

## Multiple choice • 5 to 8

Choose one answer per question.

**MC05 · §1.3**  A written sequence of steps that has not been coded is best described as what?

A. Device

B. Algorithm

C. Operating system

D. Test output

**MC06 · §1.4**  Which requirement can you test directly?

A. Make the adviser better

B. Make it intelligent

C. Ask for status if availability is unknown

D. Make it impressive

**MC07 · §1.5**  Today Room A is closed. Yesterday it was recommended. What should happen?

A. Keep yesterday’s result

B. Add a second recommendation

C. Ignore the new fact

D. Recompute from today’s facts

**MC08 · §1.5**  Which action is a regression test?

A. Rerun a saved missing-status test after editing the code

B. Write a new feature name

C. Delete all earlier cases

D. Count the files

<!--page-->

## Multiple choice • 9 to 12

Choose one answer per question.

**MC09 · §2.1**  Given Enrolled(person, course), what does Enrolled(Mina, AI101) mean?

A. AI101 teaches Mina

B. Mina is enrolled in AI101

C. Mina teaches AI101

D. Mina is a room

**MC10 · §2.2**  If A is true and B is false, what are A AND B and A OR B?

A. True, true

B. True, false

C. False, true

D. False, false

**MC11 · §2.2**  IF student THEN library access. You know that Lee has library access. Which answer is justified?

A. Lee is definitely a student

B. Lee is definitely not a student

C. No students have access

D. The rule alone does not establish whether Lee is a student

**MC12 · §2.3**  R1: quiet AND solo → suitable. R2: suitable AND open → recommend. With only quiet and solo, what is new?

A. Suitable only

B. Recommend only

C. Closed

D. Suitable and recommend

<!--page-->

## Multiple choice • 13 to 16

Choose one answer per question.

**MC13 · §2.3**  R2 is suitable AND open → recommend. To prove recommend, what does backward chaining seek first?

A. Quiet and closed

B. Suitable and open

C. A booking number

D. Recommend itself

**MC14 · §2.4**  Edges: S→A, S→B, A→G, B→C, C→G. BFS explores A before B and tests the goal on removal. What path is returned?

A. S→A→B→G

B. S→G

C. S→A→G

D. S→B→G

**MC15 · §2.4**  Edges: S→A, S→B, A→G, B→C, C→G. What path can DFS find if it follows B first?

A. S→G

B. S→B→G

C. S→A→C→G

D. S→B→C→G

**MC16 · §2.5**  Plug requires at desk and socket working. At the entrance, with a working socket, what is missing?

A. At desk

B. Socket working

C. An output screen

D. A second socket

<!--page-->

## Multiple choice • 17 to 20

Choose one answer per question.

**MC17 · §2.6**  Where does a rule-based adviser keep current case facts?

A. Knowledge base of general rules

B. Working memory

C. Screen hardware

D. The answer key

**MC18 · §2.6**  R5 requires needs_quiet_power, open_A, quiet_A and power_A. Which missing fact blocks R5 even when Mina needs quiet and power and the room is open and powered?

A. The name of the app

B. The day of the week

C. quiet_A

D. The booking receipt

**MC19 · §2.6**  Under our validation policy, what happens if open_A and closed_A are both supplied?

A. Prefer the first fact

B. Recommend anyway

C. Combine both into open

D. Reject the inconsistent case

**MC20 · §2.7**  Which design combines learned and symbolic methods?

A. Estimate noise from data, then apply explicit room rules

B. Treat every estimate as certainly true

C. Remove all checks

D. Use only the room number

<!--page-->

## Extended response • 1 to 3

Answer on a separate sheet. Label each reasoning step.

**OE01 · §1.2–1.4**  Design an adviser for one room that already meets Mina’s needs. Give an input, a processing step and an output. Write the unknown-status requirement. Test it with two inputs.

**OE02 · §1.4–1.5**  An app still displays yesterday’s recommendation after Room A closes. Give a normal test, an update test and a conflict test. How would you check a later fix?

**OE03 · §2.1–2.2**  Use Enrolled(person, course), the fact Enrolled(Mina, AI101), and IF Enrolled(x, AI101) THEN CanReadNotes(x). Show the substitution and inference. Can access alone prove enrolment?

<!--page-->

## Extended response • 4 to 6

Answer on a separate sheet. Label each reasoning step.

**OE04 · §2.3**  Use R1: quiet AND solo → suitable and R2: suitable AND open → recommend. Trace the full case forward and backward. Then remove open and start again.

**OE05 · §2.4–2.5**  Use S→A, S→B, A→G, B→C, C→G, equal costs. Trace BFS with A first, marking on enqueue and checking goals on removal. Compare DFS with B first. Then explain why Plug cannot run before Walk if Plug needs at desk.

**OE06 · §2.6–2.7**  R4: quiet AND power → needs_quiet_power. R5: needs_quiet_power AND open_A AND quiet_A AND power_A → recommend_A. Trace all five inputs, then remove quiet_A. Name the system components and one limit of the trace.

<!--page-->

## Answer key • True or false 1–10

**TF01 · True**  It is a physical component.

**TF02 · False**  It is application software: it performs a task for a user.

**TF03 · True**  The system can ask for availability instead of naming a room.

**TF04 · False**  It is a plan of steps and can be described in pseudocode or plain language.

**TF05 · True**  It specifies both an input condition and an observable response.

**TF06 · False**  An acceptable input can still be inaccurate or outdated.

**TF07 · True**  An independent expectation can reveal a wrong actual result.

**TF08 · False**  A changed input needs a separate update test.

**TF09 · False**  The first position refers to a person and the second to a course.

**TF10 · True**  It needs at least one true input and allows both.

<!--page-->

## Answer key • True or false 11–20

**TF11 · False**  The rule gives a sufficient condition for B; another condition might also produce B.

**TF12 · True**  It applies rules whose conditions are supported and adds new facts.

**TF13 · False**  It searches for rules and facts that would support that goal.

**TF14 · False**  Missing status leaves availability unknown.

**TF15 · False**  Successively removed states may lie on different branches.

**TF16 · True**  Each depth adds the same cost per action.

**TF17 · True**  A missing condition blocks that action.

**TF18 · False**  A need and a room property describe different things.

**TF19 · True**  Working memory holds the case; the engine carries out the reasoning.

**TF20 · True**  Logical support does not verify the accuracy or freshness of an input.

<!--page-->

## Answer key • Multiple choice 1–10

**MC01 · B**  The booking app performs a task for a user.

**MC02 · C**  It manages resources such as memory and devices for programs.

**MC03 · A**  The adviser receives it before applying its rules.

**MC04 · D**  Processing is the operation that transforms the supplied information into a response.

**MC05 · B**  A program is an implementation; an algorithm can exist before implementation.

**MC06 · C**  It identifies a specific input and a visible response.

**MC07 · D**  The old result must disappear when it has lost its support.

**MC08 · A**  A saved case can reveal a fault that returns after a change.

**MC09 · B**  The person is the first argument and the course is the second.

**MC10 · C**  AND needs both; inclusive OR needs only one.

<!--page-->

## Answer key • Multiple choice 11–20

**MC11 · D**  Knowing the conclusion does not prove that particular premise.

**MC12 · A**  R1 fires, but R2 still lacks open.

**MC13 · B**  It turns the two conditions of R2 into subgoals.

**MC14 · C**  G is first discovered from A; parent links give S→A→G.

**MC15 · D**  DFS can follow the deeper B branch before returning to consider A.

**MC16 · A**  Both preconditions must hold; the person has not reached the desk.

**MC17 · B**  Working memory records the case being processed.

**MC18 · C**  The room itself must be known quiet. A learner’s wish cannot supply that fact.

**MC19 · D**  A single room cannot have both statuses in this model.

**MC20 · A**  A learned estimate may inform a rule; uncertainty still matters.

<!--page-->

## Answer key • Worked responses

### OE01 · §1.2–1.4

1. Input: current availability. The suitability of the room is given in this exercise.

2. Processing: compare the supplied status with the known-open, closed and unknown branches. Output either a candidate or an informative message.

3. Requirement: when availability is unknown, ask for the status before recommending.

4. Test one: known open → offer the room. Test two: unknown → ask if the room is open and do not offer it yet.

5. These expectations come from the requirement. Writing the steps gives an algorithm; implementing them in a language gives a program.

**Check:** Credit a coherent input/process/output, an observable requirement, and both input–expected result pairs.

### OE02 · §1.4–1.5

1. Normal: begin with a suitable room known open. Expect a candidate. This establishes the starting state for the update test.

2. Update: replace open with closed, keeping other facts unchanged. Expect the old recommendation to disappear. If it remains, record the actual result as a failure.

3. Conflict: submit open and closed together. Under our policy, expect rejection before reasoning. This is different from a valid change over time.

4. Repair the update logic. Repeat the saved update test and normal test; repeating earlier checks after a change is regression testing.

**Check:** Credit expected outcomes for three distinct inputs and a concrete regression check.

<!--page-->

## Answer key • Worked responses

### OE03 · §2.1–2.2

1. The first argument identifies a person; the second identifies a course. Swapping them would change the claim.

2. Substitute Mina for x. The condition becomes Enrolled(Mina, AI101), exactly the given fact.

3. Apply the rule in its stated direction. Add CanReadNotes(Mina).

4. Now suppose only CanReadNotes(Mina) is given. Enrolment does not follow: a guest-access rule could also grant access. Equally, the absence of an enrolment fact does not by itself establish that Mina is not enrolled.

**Check:** Credit role meanings, substitution, derived fact and a justified rejection of the converse.

### OE04 · §2.3

1. Forward: start with quiet, solo and open. R1 adds suitable. R2 now has suitable and open and adds recommend. A fresh scan adds nothing new.

2. Backward: start with goal recommend. R2 needs suitable and open. R1 supports suitable from quiet and solo. Open is an input, so both R2 conditions are supported.

3. Remove open and reset derived facts. R1 still adds suitable. R2 lacks open, so recommend is unsupported. Ask whether the room is open. Do not infer closed or keep the old recommendation.

**Check:** Credit both reasoning directions, the missing condition, and the response for an unknown status.

<!--page-->

## Answer key • Worked responses

### OE05 · §2.4–2.5

1. Start queue [S]. Remove S → [A,B]. Remove A → [B,G]. Remove B → [G,C]. Remove G and stop.

2. Removal order is S,A,B,G. G was first queued from A, which was queued from S. Returned path: S,A,G. No edge joins A to B.

3. DFS choosing B first can return S,B,C,G. That uses three actions rather than two. Under equal costs the two-action BFS route is also least-cost.

4. A plan checks action preconditions. At the entrance, at desk is missing. Walk can establish it; Plug still needs a working socket after the walk.

**Check:** Credit queue trace, reconstructed path, valid DFS comparison and a precondition check.

### OE06 · §2.6–2.7

1. Knowledge base: R4 and R5. Working memory: quiet, power, open_A, quiet_A and power_A. Interface: collects the facts and displays the result.

2. The inference engine applies R4 and adds needs_quiet_power; then R5 adds recommend_A.

3. Start a new case without quiet_A. R4 still fires from the learner needs. R5 now lacks a room property, so Room A is not supported. Ask about its quietness; missing quiet_A does not establish that the room is noisy.

4. The trace explains the model’s answer. It cannot confirm whether an open_A record is current or reserve the room.

**Check:** Credit the roles, two rule traces, the learner/room distinction and one real limitation.
