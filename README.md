# lethalcompany_scrap

The goal here is to calculate the average scrap from every moon in the latest version of lethal company, currently version 50.

To use the program, you can edit the main.rs file and its variables `moon` and `number_of_runs`. These do what you would expect them to. You can download the git and use `cargo build` and `cargo run` to see results of the test.

The first line of the output is the selected moon followed by the average scrap value, the population standard deviation, and the sample standard deviation.

## Calculated Average Scrap Values From Initial Commit

- Experimentation: 301
- Assurance: 536
- Vow: 510
- Offense: 579
- March: 549
- Adamance: 669
- Rend: 1224
- Dine: 1255
- Titan: 1490
- Artifice: 2008

These numbers have been rounded and have stayed consistent in the rust version. The main change in rust is faster calculation.

## List of Things to Add

- Maybe add GUI to make use easier
