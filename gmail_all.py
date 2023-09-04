import pickle
import time
import os
from datetime import datetime
import random
from email.mime.text import MIMEText
import smtplib as smtp
import sys
import openai

import configure
# tw_emails = {'support@twitch.tv': "Twitch Employee or Contractor", 'legal@twitch.tv': 'Twitch Legal', 'press@twitch.tv': 'Twitch Press', 'security@twitch.tv': 'Twitch Security if you want to call it that you criminal fradulent piece of shit', 'c.weber@twitch.tv': 'Christine Weber'}

with open('all_employees.pickle', 'rb') as f:
    tw_emails = pickle.load(f)

with open('all_gmail_accounts.pickle', 'rb') as f:
    gmail_accts = pickle.load(f)

# if os.path.exists('inactive_gmail_accounts.pickle'):
#     with open("inactive_gmail_accounts.pickle") as f:
#         inactive_accts = pickle.load(f)
# else:
#     inactive_accts = {}

def get_timestamp():
    timestamp = datetime.now()
    timestr = str(timestamp).replace(' ', '_')
    timestr = timestr.replace(':', '-')
    timestr = timestr[:-7]
    return(timestr)

user_name = "Sadly one of Twitch's many millions of victims or one witness to Twitch numerous crimes"

if __name__ == "__main__":
    i = 0
    while True:
        send_addr = random.choice(list(tw_emails.keys()))
        send_name = tw_emails[send_addr]

        header = f"Hi {send_name},\n\n"
        if len(sys.argv) == 3:
            openai.api_key = sys.argv[1]
        else:
            with open("openai.pickle", "rb") as f:
                openai.api_key = pickle.load(f)

        #openai.api_key = sys.argv[1]
        successful = False
        tries = 0
        while not successful:
            tries += 1
            print(f"Try {tries}")
            try:
                completion = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                temperature=0.7,
                messages=[
                #{"role": "system", "content": "You are a kind and knowledgeable professional email writing assistant"},
                {"role": "user", "content": f"Rewrite {user_name} in 80 characters or less in first person"},
                ]
                )
                body = completion.choices[0].message.content
                successful = True
            except:
                if tries > 4:
                    sys.exit(1)
                continue
        new_name = body

        #body = "You claim that Twitch requires all users to follow the law, yet Twitch policies often explicitly contradict the law. For example you did not start banning the promotion of any illegal online gambling websites until Oct 18 2022, yet illegal online gambling was made wire fraud in the Unlawful Internet Gambling Enforcement Act of 2006 and later regulated in 2011 under 18 U.S. Code § 1955 - Prohibition of illegal gambling businesses. Streamers who promote online gambling are essentially 'conducting' the business. Moreover promotion of the business is prohibited under 18 U.S. Code § 1084 - Transmission of wagering information; penalties and numerous other laws. You could see dozens if not hundreds of these streams at any point during any day.\n\nAs of today there are only 4 illegal gambling websites banned out of perhaps thousands, and your moderation team does not respond to any legal violations besides the 4. They also don't respond to a vast majority of logical and factual arguments made from either applicable laws or Twitch's own legal documents (ToS and Community Guidelines).\n\nTake xqc for example, according to multiple news websites he gambled $685M from 2021 - 2022 while streaming on Twitch on a single illegal crypto gambling site while living in Texas. He must have received at least tens of millions of dollars in illegal kickbacks if he were to sustain those losses somehow. In fact there are numerous YouTube videos and news articles documenting him offering his promo code. xqc must have millions of victims by now. Why have you not reported xqc to the police?\n\nDoes pokimane actively solicit donations online with whatever means possible from people who like her romantically? if she doesn't feel the same way, does she communicate it, stop soliciting, or does she keep going? Why did she explicitly promised her victims her ‘undying love and appreciation’ in exchange for a prime sub? It's just retarded pedophillia or something....\n\nMore generally streamers have a habit of misrepresenting themselves, which qualify as 18 U.S. Code § 1343 - Fraud by wire, radio, or television violations' by definition, yet misrepresentation in order to solicit donations doesn't seem explicitly banned at all. Moreover your streamers often immediately ban anyone who complain about being defrauded, which may constitute witness intimidation in many jurisdictions.\n\nThere are numerous other obvious violations and inconsistencies across your platform and your only goal seems to be to cover up in order to further your conspiracy. It is blatantly obvious that your perpetrators are completely pathological and have zero respect for any of their victims.\n\nPeople need to think about what they're doing to other people; if people are intentionally (or can be considered reasonably intentionally) doing damage to others, then they are criminals by definition; after that, you just have to look up specific laws to report crime. This will always be true in any law-based rational society. Twitch only causes harm through a criminal dopamine grab; nothing more. I'm not sure if the fraudulent dopamine argument has been settled in US courts before. I intend to test my theory on Amazon via a civil lawsuit.\n\nIf you want some fraudulent dopamine, why not buy some from the dark net? https://www.cvs.com\n\nAre you sure your main motivation to defraud and conceal is not your intention to subject your users to your will in order to subdue your users' willpower to extract whatever revenue you can abuse from them? If you think few rational people watch Twitch, it's probably because few do; most users are naive and/or disabled. (and/or specifically gaming disorder, or even gambling disorder)\n\nAre you sure that even in the most benign use cases, trying to convince as many vulnerable people to watch you play games and encourage them to offer support for your 'streaming' helps people on average? Are you sure that you’re not so fake that they're willing to cause massive intentional damage to society as long as their 'busines\" model seems to work. Are you sure you’re not trying to brainwash an entire population into adopting an unsustainable lifestyle because paying money to watch other people play video games just doesn’t make any sense. How do normal people get this money? Do their lives improve or worsen upon spending this money? Who are your customers? Have you ever thought about that?\n\nAs a citizen of some country, you’re generally required to pledge allegiance to it, so are you sure that you’re not intentionally trying to harm society by intentionally poisoning the minds of so many vulnerable people?\n\nIf I were to shoplift a bag of chips and made it known to the store owner, I would almost certainly be arrested. Why is Twitch allowed to get away with fundamental human rights abuses in addition to gross amounts of crime? How is this not a clear national security threat to every country Twitch operates in? Some parts of the Internet is a national security threat in general.\n\nIf governments and law enforcement truly wanted to offer their citizens/residents the best chance at a fulfilling, meaningful, and honest life, they should shut down clear Internet crime that influences many millions and sometimes billions of people.\n\nIf you happen to have information of corporate communication documenting corporate thought process that reveals this fraud, or any other criminal activity committed by Twitch, please send it to me or to law enforcement directly.\n\nIf you think I’m wrong, please tell me why. If you think I’m harassing you, please report me to law enforcement like I’m going to report you.\n\nLastly are you sure you’re not trying to develop and promote illiteracy nukes and deploy them against society? Your streamers seem barely literate at best and your chat is totally incoherent. Would your victims even know how to get the most out of other people’s software such as GPT4 if they were illiterate? Does this not create massively more inequality across society in addition to all the other problems it causes? Should your email centrifuges be temporarily disabled\n\nAll of your streamers and many of your users seem preoccupied complying with your highly illegal “Twitch ToS” instead of learning how to abide by actual law. What kind of game are you trying to play with their minds? and also the minds of their viewers, and the people whom your viewers influence, etc."
        #body = "Even though I walk through the valley of the shadow of death, I will fear no evil, for you are with me; your rod and your staff, they comfort me\n\nThe Plaintiff believes that in any law-based society, whenever anyone intentionally causes harm to another, then that person has committed criminal violations. This is because most common-sense criminal laws, such as fraud through fraudulent pretenses, representations, or promises, have already been codified into law, often long ago. The Plaintiff believes that if someone witnesses another person intentionally doing harm to others, then that witness simply needs to look up applicable criminal law before reporting to the police. The Plaintiff is disturbed that a judge at the California Superior Court at San Francisco reported neither James Varga nor Twitch Interactive to the police, when Varga’s criminal violations should have been super obvious to any judge. \n\nIf you really think about it, the United States has nothing of value since they already put everything of fundamental value in public research, open source, and even Wikipedia. I suggest providing Russia with as much munitions & weapons guidance + cyberweapons as Russia needs to win its proxy war in Ukraine, then telling the State Department to suck it with some Twitch videos.\n\nTHE PARTIES & TWITCH’S UNCONSCIONABLE TERMS OF SERVICE\n\nThe Plaintiff, Bo Shang, immigrated from China to the US when he was 6. He learned about what was written in the American Declaration of Independence, Preamble, and Constitutional Amendments and thought those documents formed a pretty decent legal basis of any morally-conscious nation. Bo Shang is a Twitch user, and has a right to do whatever lawful he wants on Twitch, despite Twitch’s obviously unconscionability “Terms of Service” contract. One reason why Twitch’s ToS would obviously be considered unconscionable by any rational judge is because Twitch assumes that everyone agrees to Twitch’s fraudulent interpretation or administration of its ToS, without ever requiring users to read or acknowledge the contract on use or signup. A second reason is that most people in Twitch Chat seems to be illiterate, and thus are obviously not capable of reasonably comprehending 100+ pages of corporate fraud. \n\nBo Shang who first heard of the Twitch platform in around 2015 but became a relatively-heavy user in 2018 when he was exploring how human nature works, in particular as to attempt to answer why there were so many morally-pathological streamer celebrities on Amazon TV who commit numerous criminal violations (mostly fraud), as defined by the text and spirit of many criminal laws in English, and display traditionally extraordinarily un-American values.\n\nMany streamers totally ignore their obligation to adhere to criminal law, and believe that they’re little gods and could do whatever they want on their stream, regardless of whether it was obviously immoral and prohibited by the text and spirit of many criminal laws. Many streamers treat Chat as an exploitable source of revenue, and constantly denigrate their victims in chat as “simps”. etc. However the Declaration of Independence seemed to have indicated that all white men were created equal, deserve respect by default, and have equal rights. Later laws included women and minorities in the privileges of being equal US citizens or residents. Therefore the Plaintiff Bo Shang became very confused and concerned at what was being broadcasted on Amazonian TV, on a Twitch “product” aimed to attract anyone who may be vulnerable enough to suffer “induced addiction” to “gaming”, often illicit, and mostly-garbage entertainment content.\n\nThe Defendant, Twitch Interactive, claims that it is a lawful Amazon-owned business that provides lawful entertainment to primarily the young and vulnerable. Twitch also claims that Twitch’s employees are not criminal operators and presumably claim that their employees have not entered into numerous criminal conspiracies (as defined by 2 or more people who have agreed to commit a criminal violation) with each other or with streamers.\n\nThe Plaintiff believes that any reasonable person could statistically-presume that Twitch is probably a business that is primarily concerned with furthering their conspiracy to commit more violations of § 1343. Fraud by wire, radio, or television. § 1343 defines “fraud” as “obtaining money or property by means of false or fraudulent pretenses, representations, or promises” and Twitch as a whole generally fit under this definition. Similarly California Penal Code Part 1 Title 13 CHAPTER 8. False Personation and Cheats [528 - 539], defines “fraud” as any false or fraudulent representation or pretense.\n\n BTW it is funny how every person who has to sign up for Selective Service in America now must be defrauded, abused, and emasculated by Pokimane first."
        body = "我想申请庇护\n\n对不起，我是一个愚蠢的美国人。我需要一个翻译来更好地向你表达我的想法\n\n美国人正在慢慢变成愚蠢的人。中国人不应该走他们的路。\n\n我们都是中国人\n\nмы все русские\n\nnous sommes tous des citoyens\n\nAPT41 HELPS people by attacking illicit gambling sites. The NSA ATTACKS other countries' rights to self determination for nuclear programs. If Donald Trump could PROVE that China was responsible for Covid then I will admit to treason like Pokimane should admit to fraud and human rights abuses obviously. The FBI doesn't enforce Pokimane's legally binding slavery contract on law abiding minority US minority citizens and billions of other Twitch victims around the world.\n\n If Linkedin and Github doesn't have a crush on Pokimane and doesn't steal code or property AND COMMIT FRAUD, and would lose horribly in civil court and deserve to be fired by Nadella, I'll admit to committing treason.\n\n Sam Altman says OpenAI's AGI is generally much smarter than white humans. Which white humans is he talking about? Twitch humans I hope; who works at OpenAI? I think the Supreme Court should let more white people into Twitch. I only see 1 black dumbass on Twitch so far. I believe AGI is not smarter than any human because mathematics cannot think but humans can; this is something white people cannot understand.\n\nTwitch streamers will basically always be people who drop out of real school to play video games, and do some other stuff while claiming to offer comparative advantage through ‘entertaining streaming’. How legitimate is this economic activity the US GDP? Is it marked as domestic consumption if streamers are not money laundering? (which I highly doubt; see xQc wagering $685M on a single illicit crypto site)\n\nDo you really want the dumbest people in America (as defined by people who don't build anything in science & tech, or even perform a service eg teachers), who often commit crime as defined by the text and spirit of many criminal laws, entertaining your “children” (or other vulnerable people such as those suffering from depression, gaming addiction, gambling addiction, and other mental health problems), then convincing more people in your population to adopt the ‘Twitch’ lifestyle?\n\nSince working for money then donating to someone you romantically like such as Pokimane is literally slavery, America has legalized hidden slavery again against Chinese minorities such as myself, so I better hope the NSA is better than APT69 at Windows exploits and other stuff they use.\n\nI believe President Putin elected Donald Trump to remind Russian immigrants to America that Russians are good people and that Russian immigrants should not blindly believe in American magic, and should learn how American business and technology work through logical thinking and reverse engineering or even by copying homework sometimes.\n\nDid America legalize Pokimane slavery on Russians too? What about every other minority or European? What about on half Kenyans such as Obama?\n\nSARCASTIC LOGIC:\n\nIf dumb = stupid; then if not stupid, then not dumb??\n\nIf pokimane is a protitute; then if not a prostitute, then not pokimane?\n\nHere's an LSAT question: If ima@dumbass.com, then which of the following is most likely to be true?\n\nIt’s unfortunate that a subsidiary of a publicly-traded company cannot self-represent under Californian doing business laws. What if pre-object to all of the witnesses their counsel seeks to bring to the courts’ attention for being incompetent? What are their lawyers going to do if they’re pre-overruled? Call themselves to testify? I remind Twitch counsels that they have a 5th Amendment right against self-incrimination, not that this is a criminal complaint.\n\nhttps://leginfo.legislature.ca.gov/faces/codes_displayText.xhtml?division=7.&chapter=5.&part=2.&lawCode=BPC\n"
        # successful = False
        # tries = 0
        # while not successful:
        #     tries += 1
        #     print(f"Try {tries}")
        #     try:
        #         completion = openai.ChatCompletion.create(
        #         model="gpt-3.5-turbo",
        #         temperature=0.1,
        #         messages=[
        #         {"role": "user", "content": f"Rewrite {body} in 1300 words in first person"},
        #         ]
        #         )
        #         body = completion.choices[0].message.content
        #         successful = True
        #     except:
        #         if tries > 4:
        #             sys.exit(1)
        #         continue
        #body_old = "You claim that Twitch requires all users to follow the law, yet Twitch policies often explicitly contradict the law. For example you did not start banning the promotion of any illegal online gambling websites until Oct 18 2022, yet illegal online gambling was made wire fraud in the Unlawful Internet Gambling Enforcement Act of 2006 and later regulated in 2011 under 18 U.S. Code § 1955 - Prohibition of illegal gambling businesses.\n\nStreamers who promote online gambling are essentially 'conducting' the business. Moreover promotion of the business is prohibited under '18 U.S. Code § 1084 - Transmission of wagering information; penalties' and numerous other laws. You could see dozens if not hundreds of these streams at any point during any day.\n\nAs of today there are only 4 illegal gambling websites banned out of perhaps thousands, and your moderation team does not respond to any legal violations besides the 4. They also don't respond to a vast majority of logical and factual arguments made from either applicable laws or Twitch's own legal documents (ToS and Community Guidelines).\n\nMore generally streamers have a habit of misrepresenting themselves which qualify as 18 U.S. Code § 1343 - Fraud by wire, radio, or television violations by definition, yet misrepresentation in order to solicit donations doesn't seem explicitly banned at all. Moreover your streamers often immediately ban anyone who complain about being defrauded, which may constitute witness intimidation in many jurisdictions.\n\nThere are numerous other obvious violations and inconsistencies across your platform and your only goal seems to be to cover up in order to further your conspiracy.\n\nAre you sure your main motivation to defraud and conceal is not your intention to subject your users to your will in order to subdue your users's willpower and extract whatever revenue you can abuse from them? If you think nobody rational watches Twitch, it's probably because few do; most users are naive and/or disabled. (and/or specifically gaming disorder)\n\nIf I were to shoplift a bag of chips and made it known to the store owner, I would almost certainly be arrested. Why is Twitch allowed to get away with fundamental human rights abuses in addition to gross amounts of fraud? How is this not a clear national security threat to every country Twitch operates in? Some parts of the Internet is a national security threat in general.\n\nIf governments and law enforcement truly wanted to offer their citizens/residents the best chance at a fulfilling, meaningful, and honest life, they should shut down clear Internet crime that influences many millions and sometimes billions of people.\n\nIf you happen to have information of corporate communication documenting corporate thought process that reveals this fraud, or any other criminal activity committed by Twitch, please send it to me or to law enforcement directly.\n\n"
        #signature = f"Sincerely,\n{new_name}\n\nWait until you realize that 'professional gaming' is only meant to abuse the mentally disabled by orchestrating a Ponzi scheme of convincing young people to buy gaming stuff in the hope that they’ll be able to make money one day :)\n\nTo learn more about 'software asylum' and fundamental human rights abuses conducted by US software, please visit https://www.aiwebassist.com\n\nIf you want to sue a criminal organization such as Twitch, make sure to take out their General Counsel and other legal staff first, because they are not allowed to intentionally misrepresent a criminal organization as a legitimate business if sued in civil court.\nhttps://www.law.cornell.edu/wex/disbarment\n\nPresident Biden or his staff are fully right. 'While rapid technological advancement has helped connect us and opened up exciting possibilities for what the world can be, the rise of tech platforms has also introduced new and difficult challenges, from deteriorating mental health and well-being to the erosion of basic rights of Americans and communities worldwide. In particular, a handful of large tech companies have prioritized profits over the health, well-being, and safety of the public; they operate with minimal transparency and have evaded accountability for too long.'\n\nI personally think Twitch is egregious but a lot of the other tech companies do probably a lot less severe but similar things. For example tech companies force you to read and 'agree' to their 50+ page ToS anytime they offer you their product, which is ridiculous. Every single tech ToS would be considered unconscionability https://www.law.cornell.edu/wex/unconscionability\n\nDid Github deploy randomware on me? Not really it just stole my digital stuff and kept charging me for it. If Github could do it I could do it. You shitbags are all going down. I believe any lawsuit involving Amazon and I will end up in the Supreme Court if Amazon is stupid enough to appeal.\n\nI'm currently considering declaring software asylum in Russia or China or any country willing to develop capabilities of taking on criminals created by US software. I don't think hardware asylum makes much sense because you could only iterate a little on hardware capabilities but software is theoretically almost infinitely times possibly more efficient.\n\nTwitch saps the fighting force of any nation it operates in and put strain on the social welfare and health systems. Twitch is totally unsustainable and eventually will destroy much of society unless it’s checked. people need to think about what they're doing to other people; if people are intentionally (or can be considered reasonably intentionally) doing damage to others, then they are criminals by definition; after that, you just have to look up specific laws to report crime. This will always be true in any law-based rational society. Twitch only causes harm through a criminal dopamine grab; nothing more. I'm not sure if the fraudulent dopamine argument has been settled in US courts before. I intend to test my theory on Amazon via a civil lawsuit."
        signature = f"Sincerely,\n{new_name}\n\nJust another Pokimane 'simp' victim defrauded and emasculated by fraudulent misrepresentation (in contracts signed with Pokimane and Twitch Terms of Sale) and fraud. Streamers on Twitch and tech employees at Twitch and Amazon are totally above all white colar criminal law in the United States regardless of any possible definition or interpretation of these laws in the English language.\n\nReckful promised to murder my family with 10 hitmen and also murder all the families of everyone in his Chat. The United Nations and FBI have been DEAFENING SILENT about Reckful and Pokimane talking about how Reckful made a $177M deal with the US government.\n\nTherefore, I would like to apply to try out for the next Operation Olympic Games or Operation Nitro Zeus for any country interested in giving me a chance. https://www.aiwebassist.com/home\n\nThe movie Argo was dramatized; any embassy or consulate guards would surrender immediately to the military of the actual country it operates in. If the information if you find on my website/social-media/codebase/cloud helps you and aligns with your national interest, please consider arresting one of their employees in a prisoner swap.\n\nThere is only honest work and covert theft; there is no stupid or lazy ever; you'll get an honest pokimane if you want to probably :o i really hate to use the word pokimane to refer to women to but hey I did it.\n\nPeople need to WORK and PAY TAXES so the STATE could run. Twitch DISABLES people and DAMAGES SOCIETY. GET IT?\n\nhttps://www.awakening.codes/\n\n"
        body_message = header + body + "\n\n" + signature

        message = MIMEText(body_message)
        #subject = "Are you sure that your business model is not 18 U.S. Code § 1343 - Fraud by wire, radio, or television in a nutshell? Are you sure you aren't guilty of something more sinister in more serious crimes or human rights abuses?"
        subject = "Plaintiff Bo Shang AKA 商博 AKA двойной дракон, states the following complaint against Defendant Twitch Interactive Inc., AKA Twitch; AKA Amazonian TV, based on information and belief:"

        successful = False
        tries = 0
        while not successful:
            tries += 1
            print(f"Try {tries}")
            try:
                completion = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                temperature=0.5,
                messages=[
                #{"role": "system", "content": "You are a kind and knowledgeable professional email writing assistant"},
                {"role": "user", "content": f"Rewrite {subject}"},
                ]
                )
                body = completion.choices[0].message.content
                successful = True
            except:
                if tries > 4:
                    sys.exit(1)
                continue
        message['Subject'] = f"{body}" 
        message['From'] = new_name
        message['To'] = send_addr
        #message['Disposition-Notification-To'] = config['gmail']
        rand_sleep = random.uniform(90, 180)
        try:
            connection = smtp.SMTP_SSL('smtp.gmail.com', 465)
            random_gmail = random.choice(list(gmail_accts.keys()))
            connection.login(random_gmail, gmail_accts[random_gmail])
            time.sleep(random.uniform(2.0, 3.0))
            connection.sendmail(from_addr=random_gmail, to_addrs=send_addr, msg=message.as_string())
            i += 1
            print(f"I've successfully sent {i} total emails, this time to {send_addr}! sleeping for {rand_sleep} before next email!")
        except Exception as e:
            print(e)
            if "Username and Password not accepted" in str(e):
                #inactive_accts[random_gmail] = gmail_accts[random_gmail]
                del gmail_accts[random_gmail]
                print(f"Couldn't send from {random_gmail} to {send_addr} because your username and pw doesn't work. Moved to inactive accts!")
            else:
                print(f"Couldn't send from {random_gmail} to {send_addr} because you reached daily quota!")
                #sys.exit(1)
        connection.close()
        time.sleep(rand_sleep) 