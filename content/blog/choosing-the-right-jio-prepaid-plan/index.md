+++
title = "Choosing the right Jio prepaid plan"
description = "Choosing the right Jio prepaid plan"
date = 2022-01-07
updated = 2022-01-08
draft = false
[taxonomies]
tags = ["analysis"]
+++

Network operators have so many plans on offer these days and easily make the customer go through decision hell. I wrote a script to give me the plan details in an easy to compare way.

<!-- more -->

The script goes to the Jio website prepaid 4g plans page and gets the details of each listed plans. Then using a logic to compute attributes like `price per day` and `data_per_day` to get an apple to apple comparison across plans with different validity and data.

{{ csv2table(path="static/data/jio.csv") }}

After taking a look at the first few plans, they are all non-daily plans. Unless you are completely covered by WiFi wherever you go these plans do not make much sense. Nowadays the consumption of navigation app or a music streaming app on-the-go is not small. Just travelling between WiFi networks while commuting will exhaust your data.

Then follows the plans that are cost optimal but have lesser validity (_<1 month_), these make sense under certain circumstances.

1. You will recharge regularly and more frequently
2. You are trying out different plans or even planning to switch networks
3. Jio will continue to keep the plan or similar plan in the future
   - If Jio decides to hike the plan(s) after you recharge then it may not be cost optimal

Then finally we get the plan which has **long term validity**, **sufficient data daily** and is **cost optimal**. This is the plan that most should go for. Recharge once and forget about it till the next recharge.

Most of the plans down the list are going to vary in terms of validity, data and addons provided (_like hotstar mobile_). They are not bad plans if you need those specific features like 3 GB/day or want to use the addons. But the `price_per_day` value will show a better picture.

_Note: This sort of analysis is interesting to see the design of the marketing and sales teams. Also, if the analysis is repeated every time they plans are updated we can look at the pricing strategy. Whether plan prices are manipulated around holidays to maximize profits. Or whether there is some seasonality to the pricing strategy._

**_Disclaimer: This analysis is automatic and is not responsible for customers missing on website/app offers and discounts. Just use this as a reference. Article will update automatically._**
