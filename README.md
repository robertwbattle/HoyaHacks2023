# Visify
Project for HoyaHacks 2023 by UNCC students Robert Battle, Dylan Halstead, and Jaden Peterson

Demo:

https://github.com/gitthing03/HoyaHacks2023/assets/70990184/5057986d-1492-4547-b370-0fb782ff1aa5


## Inspiration
Despite an increasing need for computer scientists in the world, as of 2021, only 5% of high school students study computer science. While many students will enroll into computer science programs in college, this lack of prior educational opportunities can make the transition into the world of programming difficult.
We set out to create an app that can make the process of learning to code easier for students, by specifically visualizing what could otherwise be complicated data structures to beginners. Our hope was to create something that could be demonstrated by professors to their classrooms, was scalable enough to be easily improved on to suit any program's needs, and accessible enough for students to use on their own.
What it does

## What it does
Visify is a one-page web application that prompts users to upload their Python code (while making use of our custom functions), which is then interpreted and converted into data. This data is then visualized using two elements: a wide macroscopic view showing how the code's functions interact with each other on a high level, and a narrow microscopic view that shows how specific variables (in this demo, lists and dictionaries) change over time.
How we built it

## How we built it
Visify was built using two development servers - one utilizing npm for Vue components, and another utilizing Flask for backend operations. Our team worked in parallel preparing both sides of the application for one another, utilizing some open-source code and plenty of online resources along the way.
Challenges we ran into

## Challenges we ran into
Having to rewrite many aspects of the Python programming language, having to deal with the conflicts of working in parallel, small and niche issues with Python that took hacky workarounds, staying awake, and rectifying our desire to experience D.C. with our need to get the project done.
Accomplishments that we're proud of

## Accomplishments that we're proud of
We’re proud that we produced a complete product that we believe in, without cutting too many features that we initially planned on. We feel that overambition is always a problem in hackathons, and are glad that we managed to come out of the event with something that accurately resembles what we envisioned. We are also proud of our efficiency in teamwork, communication, and working parallel to one another. Each of us was using new technologies or techniques, yet we supported each other in creating our parts of the program. Working on this project has bolstered both our technical and interpersonal skills, and for that, we are proud.
What we learned

## What we learned
Dylan - I learned how to use a graphing API, a much better fundamental understanding of the inner workings of Python code, and how to be a better teammate
Robert - I learned how to use Vue, how to handle file inputs, more efficient ways to store and present data, and how to better write code when working with others
Jaden - I also got a better understanding of how Python works under the hood, how to use Vue, how to use the cytoscape graphing library, and how to better explain my thought process and understand those of others.
What's next for Visify

## What's next for Visify
We intentionally designed Visify to be extremely scalable. Adding a new type of variable tracker is incredibly easy, and often requires little code modification. We took this approach so that we could expand the native features for the app in the future, in addition to making custom implementations more feasible. Conceptually, we believe this type of application could be developed for several other languages to fit the needs of different CS programs. Different file upload options are a feasible addition, especially now that we have a good understanding of how to logically handle the input to produce the desired output. We believe that the scalability and expansive customization potential of Visify could potentially position it in computer science classes across the country, to better prepare the next generation of programmers.
