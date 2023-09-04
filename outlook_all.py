import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import random
import pickle
import time
from datetime import datetime

with open("all_outlook_accounts.pickle", "rb") as f:
    all_outlook_accts = pickle.load(f)

with open("all_employees.pickle", "rb") as f:
    employees = pickle.load(f)

def get_timestamp():
    timestamp = datetime.now()
    timestr = str(timestamp).replace(' ', '_')
    timestr = timestr.replace(':', '-')
    timestr = timestr[:-7]
    return(timestr)

user_name = "Sadly one of Twitch's many millions of victims or one witness to Twitch numerous crimes"

while True:
    smtp_server = 'smtp-mail.outlook.com' 
    smtp_port = 587 
    username = random.choice(list(all_outlook_accts.keys()))
    password = all_outlook_accts[username]

    # Compose the email
    sender_email = username
    receiver_email = random.choice(list(employees.keys()))
    subject = 'Plaintiff Bo Shang 商博 AKA двойной дракон, states the following complaint against Defendant Twitch Interactive Inc., AKA Twitch; AKA Amazonian TV, based on information and belief:'
    part_body = "我想申请庇护\n\n对不起，我是一个愚蠢的美国人。我需要一个翻译来更好地向你表达我的想法\n\n美国人正在慢慢变成愚蠢的人。中国人不应该走他们的路。\n\n我们都是中国人\n\nмы все русские\n\nnous sommes tous des citoyens\n\nAPT41 HELPS people by attacking illicit gambling sites. The NSA ATTACKS other countries' rights to self determination for nuclear programs. If Donald Trump could PROVE that China was responsible for Covid then I will admit to treason like Pokimane should admit to fraud and human rights abuses obviously. The FBI doesn't enforce Pokimane's legally binding slavery contract on law abiding minority US minority citizens and billions of other Twitch victims around the world.\n\n If Linkedin and Github doesn't have a crush on Pokimane and doesn't steal code or property and would lose horribly in civil court and deserve to be fired by Nadella, I'll admit to committing treason.\n\n Sam Altman says OpenAI's AGI is generally much smarter than white humans. Which white humans is he talking about? Twitch humans I hope; who works at OpenAI? I think the Supreme Court should let more white people into Twitch. I only see 1 black dumbass on Twitch so far. I believe AGI is not smarter than any human because mathematics cannot think but humans can; this is something white people cannot understand.\n\nTwitch streamers will basically always be people who drop out of real school to play video games, and do some other stuff while claiming to offer comparative advantage through ‘entertaining streaming’. How legitimate is this economic activity the US GDP? Is it marked as domestic consumption if streamers are not money laundering? (which I highly doubt; see xQc wagering $685M on a single illicit crypto site)\n\nDo you really want the dumbest people in America (as defined by people who don't build anything in science & tech, or even perform a service eg teachers), who often commit crime as defined by the text and spirit of many criminal laws, entertaining your “children” (or other vulnerable people such as those suffering from depression, gaming addiction, gambling addiction, and other mental health problems), then convincing more people in your population to adopt the ‘Twitch’ lifestyle?\n\nSince working for money then donating to someone you romantically like such as Pokimane is literally slavery, America has legalized hidden slavery again against Chinese minorities such as myself, so I better hope the NSA is better than APT69 at Windows exploits and other stuff they use.\n\nI believe President Putin elected Donald Trump to remind Russian immigrants to America that Russians are good people and that Russian immigrants should not blindly believe in American magic, and should learn how American business and technology work through logical thinking and reverse engineering or even by copying homework sometimes.\n\nDid America legalize Pokimane slavery on Russians too? What about every other minority or European? What about on half Kenyans such as Obama?\n\nSARCASTIC LOGIC:\n\nIf dumb = stupid; then if not stupid, then not dumb??\n\nIf pokimane is a protitute; then if not a prostitute, then not pokimane?\n\nHere's an LSAT question: If ima@dumbass.com, then which of the following is most likely to be true?\n\nIt’s unfortunate that a subsidiary of a publicly-traded company cannot self-represent under Californian doing business laws. What if pre-object to all of the witnesses their counsel seeks to bring to the courts’ attention for being incompetent? What are their lawyers going to do if they’re pre-overruled? Call themselves to testify? I remind Twitch counsels that they have a 5th Amendment right against self-incrimination, not that this is a criminal complaint.\n\nhttps://leginfo.legislature.ca.gov/faces/codes_displayText.xhtml?division=7.&chapter=5.&part=2.&lawCode=BPC\n"
    signature = f"Sincerely,\n{user_name}\n\nJust another Pokimane 'simp' victim defrauded and emasculated by fraudulent misrepresentation (in contracts signed with Pokimane and Twitch Terms of Sale) and fraud. Streamers on Twitch and tech employees at Twitch and Amazon are totally above all white colar criminal law in the United States regardless of any possible definition or interpretation of these laws in the English language.\n\nReckful promised to murder my family with 10 hitmen and also murder all the families of everyone in his Chat. The United Nations and FBI have been DEAFENING SILENT about Reckful and Pokimane talking about how Reckful made a $177M deal with the US government.\n\nTherefore, I would like to apply to try out for the next Operation Olympic Games or Operation Nitro Zeus for any country interested in giving me a chance. https://www.aiwebassist.com/home\n\nThe movie Argo was dramatized; any embassy or consulate guards would surrender immediately to the military of the actual country it operates in. If the information if you find on my website/social-media/codebase/cloud helps you and aligns with your national interest, please consider arresting one of their employees in a prisoner swap.\n\nThere is only honest work and covert theft; there is no stupid or lazy ever; you'll get an honest pokimane if you want to probably :o i really hate to use the word pokimane to refer to women to but hey I did it.\n\nPeople need to WORK and PAY TAXES so the STATE could run. Twitch DISABLES people and DAMAGES SOCIETY. GET IT?\n\nhttps://www.awakening.codes/\n\n"
    body = part_body + "\n\n" + signature

    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject

    msg.attach(MIMEText(body, 'plain'))

    random_sleep = random.uniform(90, 180)
    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()  # Encrypt the connection
        server.login(username, password)
        server.sendmail(sender_email, receiver_email, msg.as_string())
        print(f"Email from {sender_email} sent successfully to {receiver_email} on {get_timestamp()}!")
        server.quit()
    except Exception as e:
        print(f"Error: {e}")
    finally:
        print(f"sleeping for {random_sleep}")
        time.sleep(random_sleep)