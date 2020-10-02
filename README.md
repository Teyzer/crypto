# Crypto

This project is based on the Vigenere and Cesar methods of cryptography. You can both encrypt and decrypt message with the givens function in this project. You can also crack encrypted messages, as long as you have a sufficient amount of text to provide.

## Table of contents
* [Technology](#technology)
* [Main functions](#Main_functions)
* [Example](#example)

## Technology
The project is built with Python `3.8.1` and will basically work with all versions of python `3.X.X`

## Main functions

To use the function just do ``
```
Help / Usage  
  -t <target_url> : Specify the starting url ( required )  
  -m <max> : Specify the max number of page to visit ( optional )  
  --explore-all : If you want to explore not same-origin domain as well ( optional )  
                  If used, please specify a maximum too, if not the thread will be infinite  
  --only-domain : If you want to visit only the homepage of each domain ( optional )
```

## Example

If I want to render the architecture of https://github.com by scanning its first 5 pages, I would type :
`python explorer.py -t https://github.com -m 5` 
And it would render a thing like this after taking some time to get the content of the 5 first pages:
```
github.com/  
├─── github.com/  
├─── about/  
├─── about/ ─── careers/  
├─── about/ ─── press/  
├─── atom/ ─── atom/  
├─── business/  
├─── collections/  
├─── contact/  
├─── customer-stories/  
├─── customer-stories/ ─── freakboy3742/  
├─── customer-stories/ ─── jessfraz/  
├─── customer-stories/ ─── kris-nova/  
├─── customer-stories/ ─── mgm-resorts/  
├─── customer-stories/ ─── nationwide/  
├─── customer-stories/ ─── sap/  
├─── customer-stories/ ─── spotify/  
├─── customer-stories/ ─── yyx990803/  
├─── electron/ ─── electron/  
├─── enterprise/  
├─── events/  
├─── explore/  
├─── features/  
├─── features/ ─── actions/  
├─── features/ ─── actions/  
├─── features/ ─── code-review/  
├─── features/ ─── code-review/  
├─── features/ ─── integrations/  
├─── features/ ─── integrations/  
├─── features/ ─── package-registry/  
├─── features/ ─── packages/  
├─── features/ ─── project-management/  
├─── features/ ─── project-management/  
├─── features/ ─── security/  
├─── git-guides/  
├─── git-lfs/ ─── git-lfs/  
├─── github/  
├─── github/ ─── hubot/  
├─── join/  
├─── login/  
├─── marketplace/  
├─── marketplace/ ─── codacy/  
├─── marketplace/ ─── codecov/  
├─── marketplace/ ─── codefactor/  
├─── marketplace/ ─── codetree/  
├─── marketplace/ ─── coveralls/  
├─── marketplace/ ─── stale/  
├─── marketplace/ ─── zenhub/  
├─── marketplace/ ─── zube/  
├─── mobile/  
├─── mobile/  
├─── nonprofit/  
├─── open-source/  
├─── organizations/ ─── enterprise_plan/  
├─── personal/  
├─── pricing/  
├─── security/  
├─── site-map/  
├─── site/ ─── privacy/  
├─── site/ ─── terms/  
├─── team/  
├─── topics/  
├─── trending/  
└─── works-with/
```
In the example above, the software did not found any phone number or email, but here's what can be rendered when the software find phone number and/or mails in the website.

```
[+] Found following mails :  
[-] support@nordvpn.com  
[-] social@nordvpnmedia.com  
[-] press@nordvpnmedia.com  
[-] careers@nordvpn.com  
[-] press@nordvpnpr.com  
[-] business@nordvpn.com  
[-] sales@nordvpnbusiness.com
```
