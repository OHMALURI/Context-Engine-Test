# Capstone - Document Standardizer - Weekly Meet

**Meeting Date:** 26th Jan, 2026 - 1:01 PM

---

**Phoenix Bouma** *[00:00]*: Oh, hey, Ryan. 
**Phoenix Bouma** *[00:01]*: How's it going? 
**Ryan Ware** *[00:03]*: I'm good. How you doing? 
**Umar Khan** *[00:04]*: Doing good. Good. How are you? 
**Ryan Ware** *[00:07]*: Great. 
**Phoenix Bouma** *[00:07]*: Yeah, yeah. 
**Phoenix Bouma** *[00:10]*: So I can share my screen. 
**Ryan Ware** *[00:13]*: Okay. 
**Umar Khan** *[00:17]*: Can you see my screen? 
**Ryan Ware** *[00:18]*: Yeah, I can see your screen. 
**Phoenix Bouma** *[00:19]*: Okay. So basically over the last week we got basically a simple end to end, like mvp, basically. So I can show you inputting a document first. 
**Phoenix Bouma** *[00:30]*: I can just show you what this document looks like. As you can see, it's all over the place. 
**Phoenix Bouma** *[00:36]*: Then when I standardize it, we get a preview of how the document looks like. It has a title, the different headings, and the text as well. Basically how I got all the templates working was looking at our. 
**Phoenix Bouma** *[00:53]*: The template that I was sent from. 
**Phoenix Bouma** *[00:55]*: The TTG report and I was basically able to extract that template and get all the information and implement that in our backend. I can even do a test with this. But there's still some things that need to be fixed. 
**Phoenix Bouma** *[01:12]*: Say I'm going to change. Let's say change it to this. Change the font here like 20. Maybe I change this to just a bit higher. Yeah. So I'm just going to save that and close that. I'm going to put that file in here, standardize it. 
**Phoenix Bouma** *[01:37]*: As you can see, the first page is a bit messed up. So I'm going to have to add a bit more handling. As you can see, the introduction is. 
**Phoenix Bouma** *[01:46]*: Fixed, all the text and then I can download the file which I'm gonna save and I can open this. 
**Phoenix Bouma** *[01:53]*: And yeah, as you can see, like the first page, I just have to add some extra handling because the title and stuff is considered normal text. So I'm just gonna have to Same for here. Document, title. But as you can see, the introduction. 
**Phoenix Bouma** *[02:06]*: Is fixed, all the text and yeah, just everything's fixed here. 
**Ryan Ware** *[02:12]*: That looks really good. Nice. Good job. 
**Phoenix Bouma** *[02:17]*: Also, I just had to fix a bit more of the preview. It looks a bit messy still. 
**Ryan Ware** *[02:22]*: Yeah, I guess just a little bit of work to do there and then essentially. Okay. 
**Phoenix Bouma** *[02:29]*: That'S what I have on my end. I think Umar has a bit more to talk about. 
**Ryan Ware** *[02:36]*: Okay. 
**Phoenix Bouma** *[02:36]*: Yeah, let me just try to download the file and then I can share. 
**Umar Khan** *[02:43]*: My screen as well. 
**Ryan Ware** *[02:46]*: Yeah. 
**Phoenix Bouma** *[02:46]*: Also we have our winter term evaluation that's going to be in the next two weeks. So I will be sending out a link to set up the meeting information. 
**Phoenix Bouma** *[02:58]*: So I'm just going to give you. 
**Phoenix Bouma** *[02:59]*: A heads up on that. 
**Ryan Ware** *[03:00]*: Okay, thanks for the heads up. 
**Phoenix Bouma** *[03:03]*: Okay, I can now. 
**Umar Khan** *[03:11]*: Okay. Should be able to see my screen. Is that. Can you guys see my screen? 
**Ryan Ware** *[03:17]*: Yeah, I Can see it's a bit blurry. 
**Phoenix Bouma** *[03:19]*: Is it blurry? 
**Umar Khan** *[03:22]*: I don't know how to fix the blurriness. Give me a sec. Maybe it's a. 
**Phoenix Bouma** *[03:28]*: What? 
**Umar Khan** *[03:29]*: Which screen? 
**Phoenix Bouma** *[03:30]*: Can you check? 
**Gerardo Garcia de Leon** *[03:31]*: It got better for a second there. I don't know if. 
**Phoenix Bouma** *[03:33]*: Yeah, okay. 
**Umar Khan** *[03:43]*: Okay. Can you see now? 
**Phoenix Bouma** *[03:46]*: Still a bit blurry, but just let it sit. 
**Gerardo Garcia de Leon** *[03:49]*: I think, I think it just. 
**Umar Khan** *[03:50]*: Let's wait a second. 
**Ryan Ware** *[03:53]*: Is there a lot of text that we're getting? 
**Ryan Ware** *[03:54]*: I'm guessing there's some text we're going to be reading, so. 
**Umar Khan** *[03:56]*: Yeah, yeah. 
**Ryan Ware** *[03:57]*: Oh, there you go. 
**Umar Khan** *[03:59]*: There we go. 
**Phoenix Bouma** *[03:59]*: It's better. 
**Umar Khan** *[04:01]*: So basically since I'm like the system architect and whatnot, so I was just thinking of a better way to navigate the back end services. So right now we're just using or the demonstration Phoenix just showed is more of an end to end based on the front end view, but we also need the same thing from the back end view and we're designing it from each part. So right now what Phoenix really showed was the intake and the output over on here. So the file intake and then the displayed augmented file. And so what's going to happen in the back end with the. During those steps or within that time would be firstly, whatever file the user inputs will be verified to the middleware system that's going to check if, well, if the file is corrupted, if it's even the right type. 
**Umar Khan** *[04:52]*: We don't want to intake random files and promise output if it was able to read. Also reading is important authorization. If it's only like a read only file or if it's not a read only file or something, if there's something wrong with it, we want to catch it there. After that we're going to go through a preliminary classification. This is just the system reading the file and figuring out which template to assign it. We're going to have a CSV or an XML or some data file. We're still deciding on which one. Based on the model that we choose for the LLM based on the file, we're going to have a file based with a bunch of templates and what's going to happen is I believe we have somewhat of a functioning classification model right now or we're in the progress of it. 
**Umar Khan** *[05:52]*: We're just testing it out and the first, the preliminary classification is just going to read over it. It's not going to be anything too advanced, it's just going to be, hey, is this a meeting minutes or is this like an agenda or is this like a resume like what is it? And based on what it is, we're going to have a different template on the xml. From there, we can send it into the LLM with a tag notifying exactly what template it is, and that tag will be used to decode the data for the template that we're going to have on the xml. Our XML is kind of like think of a matrix with a bunch of rows of different types of templates and the classifier is going to just tell us which row to use. 
**Umar Khan** *[06:41]*: Like, hey, use this exact template, don't use the other ones. Once the LLM is done, we want to add some sort of verification or a validation actually, before it's displayed to the user, because hallucinations happen and we want to make sure the system is a little more resilient to hallucinations. So we'll have a validation classification, which is going to be another model, pretty basic, but it's just going to see, hey, does this new file match the template that I've already been given? And it'll be a yes or no. It's just a classification, like yes or no. If it's a yes, it'll be displayed to the user, and if it's not, then it'll be sent back. 
**Ryan Ware** *[07:25]*: And question there again. 
**Umar Khan** *[07:27]*: Yeah. 
**Ryan Ware** *[07:28]*: So the LLM is going to be outputting text. Correct. So is this yes, verification going to. 
**Ryan Ware** *[07:35]*: Happen after the document has been formed? 
**Umar Khan** *[07:41]*: Which very. You mean the verification or. Sorry, validation? 
**Ryan Ware** *[07:45]*: Yes, the validation. 
**Phoenix Bouma** *[07:46]*: Yeah, yeah. 
**Umar Khan** *[07:47]*: So the validation is going to be after the document is formed. 
**Ryan Ware** *[07:50]*: Got you. So it's going to be more of. 
**Ryan Ware** *[07:52]*: Like a photo of the document then? 
**Umar Khan** *[07:56]*: Not exactly. So the way we can run the model is. Or the LLM or not the LLM, the model for classification for validation is just going to be. Oh, did my screen just unscrew? 
**Phoenix Bouma** *[08:12]*: Yeah, that's my bad. 
**Ryan Ware** *[08:17]*: Now you're good. 
**Phoenix Bouma** *[08:19]*: Is it showing now? 
**Ryan Ware** *[08:21]*: So you're not using an LLM for validation, you're using something else. 
**Ryan Ware** *[08:26]*: Okay. 
**Umar Khan** *[08:27]*: Just because an LLM is going to again, reduce the whole illustration back into the system and we want to make sure we take that out. All the validation is going to do is be like, okay, I just want to make sure you didn't accidentally flip title from text. I want to make sure you didn't accidentally move the picture somewhere randomly. In the demo that Phoenix just gave, you saw how all of the, like, the front page, the first page was split into two pages all of a sudden. That could be a type of hallucination that we could See, and so we want to make sure that things like that get caught. Like I would say, like stupid mistakes get caught before a human sees them because it'll also increase like the trust in the system as well as those things should all. 
**Umar Khan** *[09:18]*: Like, those are pretty easy things to get caught just by a class. Like for example, like a simple thing would be in preliminary, if it has four pages, it should not have 10 pages by the validation stage. If it had like five titles in preliminary, it should not have 20 titles by validation. Simple checks like that. 
**Ryan Ware** *[09:42]*: I see. 
**Ryan Ware** *[09:45]*: Okay. 
**Ryan Ware** *[09:48]*: So you're going to be comparing it against something. What are you going to be using? Is this a machine learning model you're going to be using for validation? 
**Umar Khan** *[09:55]*: Yes. 
**Ryan Ware** *[09:56]*: Okay. 
**Umar Khan** *[09:57]*: And the exact machine learning model we're going to be. Or I'm going to be conferring with our course. I forgot what the exact title is, but the academic advisor. Academic advisor. There you go. I'm going to be conferring with her tomorrow about the exact models we can use and how we can even simplify or if there's any steps that we need to add to make sure that there's. Basically what I'm. The validation step is more of a filter to catch anything that's not. Okay. I want to get her thoughts on that because preliminary is going to be basic bag of words, like a very basic machine learning classifier, whereas validation might have to be like a more complex one, maybe Bert or maybe something that has more contextual or time based knowledge. 
**Umar Khan** *[10:54]*: So I'll get our opinion on what to use and if there's anything that needs to be added to the system. 
**Ryan Ware** *[11:01]*: Okay. 
**Ryan Ware** *[11:01]*: Yeah, I'm interested to see how you. 
**Ryan Ware** *[11:03]*: Guys are going to do that. Okay. 
**Ryan Ware** *[11:08]*: So the LLM based augmentation, because this is a concern that Sebastian had. 
**Ryan Ware** *[11:16]*: When were, when were talking about this a couple weeks ago. 
**Ryan Ware** *[11:24]*: What exactly is the LLM going to be? What's it going to be doing to the document that gets input? 
**Ryan Ware** *[11:31]*: Guessing it's going to be. 
**Ryan Ware** *[11:32]*: It's going to have to rearrange it. 
**Ryan Ware** *[11:33]*: Into a format based on whatever template it's. 
**Ryan Ware** *[11:40]*: It's using. 
**Phoenix Bouma** *[11:40]*: Right, exactly. 
**Ryan Ware** *[11:43]*: So I'm just wondering if any of the content is going to be rewritten or altered. 
**Umar Khan** *[11:52]*: As far as that we can. I've played, I've tried to play around with some prompt engineering this last few weeks and there are prompts that you can specifically tell the LLM not to. Not to change anything, especially not to change any contact content, change fonts, change customization, do not Touch the content, make it read only things like that. Obviously it'll still hallucinate. That's not 100%. That's why the verification steps there, but the content itself there, it's. It's not like a concrete thing, especially with the LLM. I don't think anything with LLMs is concrete, especially as, like. Especially when we're talking about, like, generative AI. It's not going to specifically be generating pictures, but it would still be generating a document with the right formatting. But as far as the content, firstly as security, it's going to be an internal LLM. So that's not. 
**Umar Khan** *[12:53]*: Not that big of a concern, I would say. But as far as changing the words around, we still have the original saved on your. We still have the original, and we still. And we'll have the augmented file as well on hand, so we can always compare them within the filtering or the validation step. 
**Ryan Ware** *[13:12]*: Okay, nice. All right, then that's all the questions from me for you. I know we spoke the other week about me getting you a template for a project proposal. 
**Ryan Ware** *[13:28]*: That was a couple weeks ago. Now. 
**Ryan Ware** *[13:31]*: I'll make sure to get that to you guys for the end of the day. 
**Ryan Ware** *[13:36]*: I'll have to run it past Sebastian just to get a confirmation on it because you're going to be using it for another app of ours. But, yeah, that was my action item. Sorry it's late, guys. I apologize for that, but I'll make sure to get that to you guys sometime today, hopefully. 
**Umar Khan** *[13:55]*: Good. 
**Gerardo Garcia de Leon** *[13:56]*: And then, Ryan, I think last time that we spoke to, were talking about getting a different type of document. We were talking about having a proposal type of document and then another type just so that we could have a classification model for both. Did you happen to discuss with Sebastian what the other type of document was going to be? 
**Ryan Ware** *[14:13]*: Gosh, yes. So we haven't figured out. 
**Ryan Ware** *[14:18]*: No, we haven't figured out another. Another document to give you guys or another, like, standard, like, template to give you guys. So it would just be the project proposal for now, but I'll. I'll mention it to him again today and we'll see if we can. We'll see if we can figure something out. 
**Umar Khan** *[14:36]*: Okay, Sounds good. Yeah. 
**Ryan Ware** *[14:37]*: Yeah. 
**Ryan Ware** *[14:38]*: Sorry about the wait, guys. 
**Umar Khan** *[14:40]*: All good. 
**Gerardo Garcia de Leon** *[14:41]*: Thank you. 
**Ryan Ware** *[14:42]*: Yeah, yeah. 
**Ryan Ware** *[14:44]*: Okay, I guess that wraps this up. Did you guys have any other questions for me? 
**Umar Khan** *[14:50]*: I don't have any. 
**Phoenix Bouma** *[14:51]*: Does anyone else have any? 
**Ryan Ware** *[14:55]*: All right. 
**Ryan Ware** *[14:57]*: Okay. 
**Ryan Ware** *[14:57]*: Thanks for coming. 
**Phoenix Bouma** *[14:58]*: Yeah, yeah. 
**Ryan Ware** *[14:59]*: Thank you. And when you guys do move on to the LLM part, we do like we host our LLMs internally. 
**Ryan Ware** *[15:08]*: So there's some documentation on that inside. 
**Ryan Ware** *[15:10]*: Of the. 
**Ryan Ware** *[15:12]*: Standards and policies in the onboarding folder that were shared with you. 
**Ryan Ware** *[15:16]*: Guys, your Google Drive. So when. 
**Ryan Ware** *[15:18]*: When you guys do get to that point, you guys can take a look at that, and if you have any questions and just. Just let me know. 
**Umar Khan** *[15:24]*: Yep. Thank you. 
**Phoenix Bouma** *[15:25]*: I've already looked at documents and let them know, so. 
**Ryan Ware** *[15:28]*: Okay. Solid. Cool. All right, guys, well, I'll talk to you guys next week, then. 
**Phoenix Bouma** *[15:33]*: All right, See you, Ryan. 
**Umar Khan** *[15:34]*: All right, thank you, Ryan. 
**Ryan Ware** *[15:36]*: Thanks, guys. Bye. 
