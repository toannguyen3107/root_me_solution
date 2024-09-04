# Solution to the problem root-me: API: Broken Access 2
`link challenge`: https://www.root-me.org/en/Challenges/Web-Server/API-Broken-Access-2?lang=en
## API vuln: 
 - url: http://challenge01.root-me.org:59091/api/profile?secret=<secret>
 - method: GET
 - I see if we have secret, we can read note! (dont check permission) => crack `uuid`
 - this uuid is v1, it get timestamp (nanoseconds) from 1582-10-15 00:00:00 and mac address (02:42:AC:11:00:1A)
 - run `python sol.py` to get uuid and use it to read flag in note.
