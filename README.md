# Forward-Assault-Credit-Script
a vulnerability that works on pc version of forward Assault, works for mobile accounts as well. 

pastebin.com/qCUYDHSC

THE TUTORIAL:https://streamable.com/ei0wo2

How it works?

well for some reason blayze games's forward assault remix on computer lets you edit the information going to the server
for whatever reason with a simple python http request.
the reason for the script for being more than 100 lines is because i wanted to make it seem nice and easy to use
when watching the video. the reason the script failed last time is because no one could find the pubg.
this time i made it easy to understand.

All alright hello, this is CaeSer, how are you?

well, I don't care. anyways, if this is AceCrown reading this,

I dislike you because of how you act

Anyways, the reason I made this script is the same as the help screen on the screen, I wanted to make credit exploitation simple and easy.

Also, making a video tutorial would probably help you.


anyways, this is the last thing I'm making for Forward Assault.

Credits:

maxjg - homo

revenant - a good friend

thunder - a challenge

ark - toxic doink I like playing with

AceCrown - toxic doink that did little to no actual programming and talked about it more lol

doom - the 2 days that we were exploiting and finding new things about the game were the best it was so much fun.


i wasted 2 days trying recon shit and find information on the game:

crazygames.com contacted inside itself for the files of the game located at
/files/23/

files that the JSON linked to

FARemix.json

FARemix.asm.framework.unityweb

FARemix.asm.code.unityweb

FARemix.asm.memory.unityweb

FARemix.data.unityweb.

files were encrypted with brotli(lossless compression, mostly used for files transfer in HTTP FTP)

the only file that was useful was, "FARemix.asm.code.unityweb"

the way I decrypted the was with using xxd -d "file-name" > FARemix.asm.code.unityweb.file

then i used wxHexEditor, i used a way to find "HTTP", ".php", "blayzegames", then i saved them.

a friend of mine [doom], also found their phpmyadmin admin panel https://fa.blayzegames.com/phpmyadmin/index.php - up to date

I didn't try to brute-force it because I don't really want to take over their server, just wanted to
see how far I can go until I'm stuck. doom also found 21 potential SQL, but all of them were/js/

using sqlmap -u "https://fa.blayzegames.com/" i searched for vulnerabilities, i also searched for vulnerabilities on other servers like
testserver., testserver2. and dev-play. - all of them were up to date

also using a site "leakpeek", I searched for dev passwords - nothing came up [could be due to the server not allowing login sessions for me for some reason so that's not 100%]

also, I used my own script to try to sqli one of the servers that had MySQL

I found that fa.blayzegames.com was 2.4.38 that is vulnerable to local privilege escalation but I don't have enough time to work on it. link to the vulnerability e
xploit-db.com/exploits/46676


links and php files:
http://blayzegames.com/suport ?

https://assetbundles.blayzegames.com/Camos/camosWebGL.txt

https://dev.playforwardassault.com

/AssetBundles_ForwardAssaul/Camos/camosWebGL.txt

https://fa.blayzegames.com/accept_member_request.php?&requiredForMobile=leadernameleaderpasspubpacceptRequestPHP

fa.blayzegames.com/OnlineAccountSystem_NewFPS

Freward_for_rewards.php?userIdtimestamprewardevent_id

/buyattachmentV2.php?weaponattachmentTypeattachmenterrorInvalidKe

/buycamosV3.php?0000validityCase

/buycases.php?amount

/buycredits.php?

/buyglovesV2.php?gloveID

/buygoldcrateV3.php?weaponscamosisWeaponCamorarityId

/buyweaponV3.php?guntobu

/get-player-punishmentV2.php? !! check this, might be a way to circumventate a ban

/checkwebglversion.php?WebGL

/get_clan_membersV2.php?clan_idsearchKeydd MMM HH:mmMyClan

/clear_clan_requests.php?

/create_clan.php?clan_nameclan_tag

/get-account-roles.php?

/get_invitations.php?

/get-punish-reasons.php?

/invite_player.php?

/clan_join_requestsV2.php?

/join_clan.php?

/get-kill-rewards.php?000

/get_clans.php?

/opencase.php?camo

/reward_for_rewards.php?statusrepeated

/pass_leadership.php

/set-player-punishmentV2.php?mod_password mod_username hours reason !! check 

this, might be useful

/remove_member.php?

/report-cheater-by-player.php?detailsvideo_url

/change_clan_name.php?

/change_clan_color.php?new_tag_color

/change-username.php?username_new

/set_clan_message.php?message

/get_requested_clans.php?

/reset-player-punishmentV2.php?unmutedPlayer

/reward-click.php?video_id

/senderrorreport.php?subjectupload-screenshot

/set_clan_status.php?

/startcrateunlockV2.php?crateInde

changeemail.php?

/changepassword.php?newemailnewpassword

/getregistrationform.php?

/checkloginNEW.php?

/requestpasswordreset.php?

/registerCHANGED.php?

/setaccountinfoNEW.php?

/getaccountinfoWebgl.php?

All hard coded API endpoints

this help me!

https://www.scribd.com/document/383747951/Interesting-Forward-Assault-SOME-hardcoded-client-data-13-07-18-Liderluigi

dev commands:
/username /blacklist /restart /kick /ban /mute /unmute /unban /unmute

known devs of forwarding assault, hardcoded for whatever reason client-side LOL

devs: - go brute force their passwords lmao

polosatiy - dev

nxtboyiii - dev

alexkazam - dev

xToastii - dev
