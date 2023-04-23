# lunch_alert a KRL web application

This is described in the [Scheduling events](https://picostack.blogspot.com/2022/11/scheduling-events.html) post
of the [PicoStack](https://PicoStack/) blog.

## to run this application

1. Install a pico engine and start it
2. Visit the developer UI
3. Make a pico
4. Install the `html` ruleset
5. Install the `org.picostack.get_me_ribs` ruleset
6. Find the Event Channel Identifier (ECI) for the channel tagged "ribs_on_menus"
7. Visit the application at http://localhost:3000/c/ECI/query/org.picostack.get_me_ribs/ribs_on_menu.html (substituting in the actual ECI value)
8. Create a webhook for a Teams channel
9. Install the `teams.webhook.messaging` ruleset configured for the webhook
10. Turn on morning notification

## helpful links

For step 1, see [installation instructions](https://github.com/Picolab/pico-engine/tree/master/packages/pico-engine#readme).

For step 4, find the `html.krl` file in this folder, click on its Raw button, copy the URL from the browser location bar, and paste it into the 
URL box in the "Install Ruleset" section of the "Rulesets" tab of the developer UI.

For step 6, find the channel on the "Channels" tab of the developer UI, double-click on the identifier next to `ribs_on_menus` tag.

For steps 8 and 9, follow along in the [Notifications](https://picostack.blogspot.com/2022/12/notifications.html) post of the PicoStack blog.

For step 10, click on the gear icon (upper right corner) to see the Settings page, and then turn on morning notification.
