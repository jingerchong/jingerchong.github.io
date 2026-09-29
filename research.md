---
layout: default
title: Research
permalink: /research/
---
## NOW

I'm currently drafting my PhD thesis proposal on human intent prediction for autonomous navigation, as part of the [Center for Complex Engineering Systems (CCES)](https://cces.mit.edu/), a collaboration between MIT and King Abdulaziz City for Science and Technology (KACST) in Saudi Arabia. Robots that move through spaces shared with people need to anticipate where those people are going, not just react to where they are. My work focuses on the conditions that make this hard in practice: predictions that run in real time on board the robot, environments that change as the robot moves through them, and uncertainty estimates that a planner can use to stay safe.

<div class="industry-list" markdown="0">
{%- for item in site.data.research %}
{% if item.current %}{% include industry-item.html item=item position=item %}{% endif %}
{%- endfor %}
</div>

## BEFORE

<div class="industry-list" markdown="0">
{%- for item in site.data.research %}
{% unless item.current %}{% include industry-item.html item=item position=item %}{% endunless %}
{%- endfor %}
</div>
