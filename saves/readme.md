# Save Folder
Truss saves will be placed here.

___

Tower Notes:
- Spans 20 cm x 20 cm.
- Bonus points for spanning a 20 cm diameter circle holding at least 15 kg.
- Loading block at least 60 cm up.
    - The loading block itself has a base of 5 cm x 5 cm and is 2 cm high.
- Design logs must use the template.
    - Three unique towers tested beforehand.
    - 25% more points if log is complete.
- Maximum 15 kg / ~150 N load.
- 150 / 4 = 37.5 N load per side.

Additional Notes:
- The thickest balsa wood member shall be 1/4" x 1/8".
- Baseline Strengths:
    - Tensile: 13.9 N
    - Compressive: 139.0 N
- Baseline Strengths at 1.00 GPa (tensile and compressive):
    - 20.0 N
- Effective Strengths (tensile and compressive);
    - 40 N, for some reason...
- The critical load for a member of length 20 cm is 12.54 N.
    - Recall that halving the length will increase the critical load by x4.
- Four of 6.24 cm spacing...

Old Simulator Instructions:
> Basic Instructions for Simulator (see link somewhere above, specific to this year's parameters):
> 1. Go adjust the plane dimensions. - `Display & Dimensions` --> `Physical Dimensions` --> (click values to modify them) cm, N, 60 cm by 30 cm, snap 1 cm, 10 N. Move X and Y axis to your liking.
> 2. Place starting nodes. - `Design` --> `Add` --> `Node`. You need two with the same Y coordinate at 49 cm apart, but no more than 51 cm.
> 3. Place critical supports. - `Support (Pin)` goes on one node and `Support (Horiz. Roll)` goes on the other.
> 4. Place more `Node`s. - Make a bridge.
> 5. Place `Member`s / beams. - Make a bridge.
> 6. Add a `Force`. - There should be at least one node in the middle of your bridge no higher than 1 cm above the first two nodes you placed. Use this node as a base for your force. For specificity, your force should also be facing downwards, not upwards.
> 7. Resolve errors. - `Truss is not statically determinate.` = "Your bridge is wobbly." | `Try adding / deleting # members.` = "Do this and M = 2 * N - 3".
> 8. Decrease the force (because it's negative / downwards) until one of the members surpasses 160 N.
> 9. Judgement. - If your force distribution contains arrows that go off the screen it means it's not a good bridge. Otherwise, calculate the "*efficiency*": **N / (Σ√(xi² + yi²) + 2 * Σ√(xj² + yj²) + 4 * Σ√(xk² + yk²))**. Where **N** is the total force supported and tables **i**, **j**, **k** contain the base lengths and heights (|ΔX| and |ΔY|) for the members that hold <= 40 N, <= 80 N, and <= 160 N, respectively.
