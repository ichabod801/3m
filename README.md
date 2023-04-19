# Frequency calculations for 3M tables.

So I'm working on the Gygax 75 challenge by Ray Otis. In part 2, the surrounding area, you make an encounter table for the area. The table uses a 2d6 roll, and he advises putting the weaker encounters in the middle of the range, so they are more common.

That's all well and good, but I have a trade road moving through my area. I was thinking I should have one table for the road and one table for off the road. But there would be some overlap between the two tables, and I was trying to think of a way to make one table. Then I remembered the dice mechanics of Silent Death (an old spaceship combat game), and came up with 3M tables. Although I would not be at all surprised if someone else came up with this idea previously and called it something else.

For a 3M table, instead of rolling 2d6, we roll 3d12. But the table rows are 1-12, similar to the 2-12 you would see with 2d6. Instead of putting the weaker encounters in the middle of the range, we put the weaker/road encounters in the lower numbers. We put the tougher/wilderness encounters in the higher numbers. You roll the 3d12, and if the encounter is on the road you take the lowest d12 (the minimum). If you are in the wilderness off the road, you take the highest d12 (the maximum). If you are near the road, but not quite into the deep wilderness, you can take the middle d12 (the minimum, the medium, and the maximum are why I call it a 3M table). These three options give you a weak encounter on the road, and tough encounter in the wilderness, and a mix of encounters if you are near the road, all from the same table. The exact frequencies of the rolls are below:

| Result | Min | Med | Max |
|--------|-----|-----|-----|
| 1      | 397 |  34 |   1 |
| 2      | 331 |  94 |   7 |
| 3      | 271 | 142 |  19 |
| 4      | 217 | 178 |  37 |
| 5      | 169 | 202 |  61 |
| 6      | 127 | 214 |  91 |
| 7      |  91 | 214 | 127 |
| 8      |  61 | 202 | 169 |
| 9      |  37 | 178 | 217 |
| 10     |  19 | 142 | 271 |
| 11     |   7 |  94 | 331 |
| 12     |   1 |  34 | 397 |

The above table has absolute frequencies. The relative frequencies for min and max run from 23%, 19%, and 15% down to 1%, 0.4%, and 0.06%. For medium the edges are 2%/5% and the middle is 12%. You could also do a 2M table, where you are basically rolling a disadvantage or advantage depending on whether you are on the road or not:

| Result | Min | Max |
|--------|-----|-----|
| 1      |  23 |   1 |
| 2      |  21 |   3 |
| 3      |  19 |   5 |
| 4      |  17 |   7 |
| 5      |  15 |   9 |
| 6      |  13 |  11 |
| 7      |  11 |  13 |
| 8      |   9 |  15 |
| 9      |   7 |  17 |
| 10     |   5 |  19 |
| 11     |   3 |  21 |
| 12     |   1 |  23 |

In this case the relative frequencies are a straight line from 16% to 0.7%.

Obviously, you can use something besides a d12 as well. I expect the curves in the 3M results would be more pronounced with larger dice and less pronounced with smaller dice. The 2M results will be straight lines regardless of the dice used.
