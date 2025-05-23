from telethon import TelegramClient
from telethon.tl.functions.account import ReportPeerRequest
from telethon.tl.types import InputReportReasonSpam
import asyncio
import time

# Telegram API credentials
api_id = '...'
api_hash = '...'
phone_number = '....'

# Target channel username
target_username = '@channel name'

# 3 report messages
report_messages = [
    """SUBJECT CLARIFICATION:– IMPORTANT NOTICE.

DEAR TELEGRAM TEAM AND CHANNEL MEMBERS, AND TELEGRAM ALL MODRATERS.
I AM REPORTING THIS ACCOUNT/CHANNEL/GROUP FOR VIOLATING TELEGRAM'S TERMS OF SERVICE BY PROMOTING OR ENGAGING IN ABUSIVE, ILLEGAL, OR HARMFUL ACTIVITIES. THE CONTENT INCLUDES, BUT IS NOT LIMITED TO, UNAUTHORIZED USE OF OBB FILES, DISTRIBUTION OF HACKED OR MODDED APPLICATIONS, AND FEATURES THAT SUPPORT ILLEGAL ACTIONS SUCH AS DATA THEFT, FRAUD, OR PRIVACY VIOLATIONS.
THIS CHANNEL IS ENGAGED IN THE DISTRIBUTION OF ILLEGAL FREE FIRE OBB FILES. THIS ACT CONSTITUTES A SERIOUS VIOLATION OF COPYRIGHT LAWS AND PIRACY REGULATIONS.
THIS ACTIVITY IS A SERIOUS SECURITY THREAT TO USERS AND UNDERMINES THE INTEGRITY OF THE PLATFORM. I STRONGLY URGE THE TELEGRAM MODERATION TEAM TO ENFORCE A PERMANENT BAN ON ANY CHANNEL THAT PROMOTES ILLEGAL CONTENT, AND ENSURE SUCH BANS ARE CARRIED OUT WITHIN 24 HOURS TO PREVENT FURTHER HARM.

THANK YOU FOR YOUR PROMPT ATTENTION TO THIS MATTER.
@telegram @AbuseNotifications @SpamBot""",

    """This channel is distributing pirated OBB files, which are unauthorized copies of Android games and applications. It is engaging in illegal activity by promoting and selling cracked apps and games without the permission of the original creators. This violates copyright laws and Telegram’s terms of service. Immediate action is needed to prevent further piracy and protect the rights of app developers.""",

    """This channel is distributing modified APK files that promote hacking and illegal activities. It encourages users to download malware or tools for unethical use. Please review for policy violations."""
]

async def report_user():
    client = TelegramClient('report_session', api_id, api_hash)
    await client.start(phone_number)
    entity = await client.get_entity(target_username)

    for msg_index, message in enumerate(report_messages, start=1):
        print(f"\n[+] Sending 1000 reports for Message {msg_index}...\n")
        for i in range(1000):
            await client(ReportPeerRequest(
                peer=entity,
                reason=InputReportReasonSpam(),
                message=message
            ))
            print(f"[{msg_index}] Report {i + 1}/1000 sent")
            time.sleep(2)  # 2 second delay

    await client.disconnect()
    print("\n[✓] All 3000 reports sent successfully.")

if __name__ == "__main__":
    asyncio.run(report_user()
