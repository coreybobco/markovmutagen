## What is Text Vomit?
Text Vomit is a basic command-line tool for "uncreative writing." Give it some text input, and Text Vomit will build a data structure (really, a probability table) for that input that looks something like this:

>[word] -> [next_word] : [number of times next_word followed word in text input]

For example, consider this text input:

>The dog jumps and runs. The boy jumps high. The boy loves to take his dog to the park.
  
This would yield the following Markov Chain probability table:
* The 
    * dog: 1
    * boy: 2
* dog 
  * jumps: 1
  * runs: 1
  * to: 
* jumps
  * and: 1
  * high: 1
* and
  * runs: 1

And so forth. 

Text Vomit will then use that data structure to generate output. It also keeps track of what words begin sentences and clauses, so when it outputs a word that ends a sentence, like a period, exclamation mark, or question mark, it next picks a word that began a sentence in the original passage. Likewise for clauses. To generate output then, Text Vomit picks a word which began a sentence in the original passage and then picks a random word which followed that word in the original passage, with words that followed it more often being weighted heavier. So the original output would yield something like this.

>The dog to take his dog to take his dog jumps high. The dog to take his dog jumps high. The boy jumps high. The boy jumps and runs.

##Installation and Setup
- Download and install the latest version of Python 3: https://www.python.org/downloads/
- Open a terminal shell (CMD.exe or Power Shell on Windows, Applications->Utilities->Terminal on OSX)
- Navigate to the directory where you have downloaded and extracted Text Vomit, probably something like: "cd Downloads/Text-Vomit/"

##Usage / Examples
Start Text Vomit in a terminal with python3.4 textvomit.py and any of the arguments below. Once it is started, you will be prompted to input (paste or type) text. To indicate you are finished inputting text, press enter and then Ctrl-C.

Generate 400 words of Markov chain based text using the -m or --markov flag.
```bash
python3.4 textvomit.py -m 400
python3.4 textvomit.py --markov 400
```

Generate a Markov chain based poem that is 200 words long using the -p or --poem flag. This currently only works in conjunction with Markov chains.
```bash
python3.4 textvomit.py -m 200 -p
python3.4 textvomit.py --markov 200 --poem
```

Cut-up Technique simulator: Break words into blocks of words between sizes 4 and 9 and rearrange the blocks.
```bash
python3.4 textvomit.py -c 4 9
```

Chatlog mode: Chatlog mode accepts text formatted in IRC log format as input, i.e.:
> \<person1\> Hi are you a bot?

> \<person2\> Maybe, I've forgotten by now. What is your credit card number?

It will then generate a chatlog using Markov chains.
```bash
python3.4 textvomit.py -m 500 -cl
```

##Things To Try
- You can paste together quotes from a couple different inputs for comic effect. For example, Nixon's resignation speech with descriptions of Reptilian shapeshifters.
- Replacing different words from copied material with the same word before running it through the Markov chain text generator can yield interesting results since it increases the probability that word will appear in the output and also causes the output to jump around more.
- You can paste in a whole novel if you want, but right now Text Vomit has no way of differentiating different paragraphs or chapters from one another, so the results are generally anarchic and unreadable. The best input length is usually 2 or 3 paragraphs worth of material.

##Artistic Inspiration
- Brion Gysin's Cut-Up Technique: http://briongysin.com/?p=157
- Kenneth Goldsmith on Uncreative Writing: http://chronicle.com/article/Uncreative-Writing/128908/
