# Bit-Error Correction
### Background -
[Bit errors](https://en.wikipedia.org/wiki/Error_detection_and_correction) occur when data bits are undesirably flipped during transfer. Causes include *network interference, hardware failure/deterioration, etc.* [Hamming codes](https://en.wikipedia.org/wiki/Hamming_code) are error-correcting codes capable of reversing single-bit errors by padding messages with [parity bits](https://en.wikipedia.org/wiki/Parity_bit). In addition, non-systematic encoding allows Hamming codes' efficiency to grow exponentially as message length increases.
<br>
| **Data Bits** <sub>( 2<sup>m</sup> - m - 1 )</sub> | 1 | 4 | 11 | 26 | 57 | 120 | 247 |
| :----: | :----: | :----: | :----: | :----: | :----: | :----: | :----: |
| **Efficiency** <sub>(Data vs. Total Bits)</sub> | 33% | 57% | 73% | 84% | 91% | 95% | 97% |

<img src="https://www.gaussianwaves.com/gaussianwaves/wp-content/uploads/2020/07/Systematic-and-non-systematic-encoding.png" width="600"></img>
<br>
### Contribution -
An autoscaling Hamming encoder/decoder to correct single-bit errors while maximizing storage efficiency. Errors are simulated over a TCP transmission and rectified by the receiver. Note: we establish an upper bound of 247 data-bits per chunk (97% efficient) to prevent 2-bit chunk errors.
