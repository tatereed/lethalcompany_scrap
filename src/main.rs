use csv::Reader;
use meansd::MeanSD;
use rand::{distributions::Distribution, distributions::WeightedIndex, thread_rng, Rng};
use std::fs::File;

fn get_csv_data(filename: &str) -> Reader<File> {
    let result = Reader::from_path(filename);

    /* One of my two times actually doing error handling */
    if result.is_err() {
        println!("Failed to read csv file.");
        std::process::exit(1);
    }
    result.unwrap()
}

fn get_scrap_amounts(moon: &str) -> u64 {
    let mut rng = thread_rng();
    /* Feel like there mights be a better way to do this, but I've got no clue */
    match &moon[..] {
        "exp" => rng.gen_range(8..12),
        "ass" => rng.gen_range(13..16),
        "vow" => rng.gen_range(12..15),
        "off" => rng.gen_range(14..18),
        "mar" => rng.gen_range(13..17),
        "ada" => rng.gen_range(16..19),
        "ren" => rng.gen_range(18..26),
        "din" => rng.gen_range(22..26),
        "tit" => rng.gen_range(28..32),
        "emb" => rng.gen_range(11..16),
        "art" => rng.gen_range(31..38),
        _ => {
            println!("Problem in get_scrap_amounts()");
            std::process::exit(1);
        }
    }
}

fn get_possible_scrap_weights(filename: &str, moon: &str) -> Vec<(f64, f64)> {
    let mut scrap_and_weights: Vec<(f64, f64)> = Vec::new();

    /* WHY DOES THIS ONE HAVE TO BE MUTABLE. NOTHING CHANGES VISIBLY. I DON'T GET IT */
    let mut rdr = get_csv_data(filename);

    for record in rdr.records() {
        /* There's the other error handling */
        if record.is_err() {
            println!("Problem reading record.");
            std::process::exit(1);
        }
        let row = record.unwrap();
        if row.get(3).unwrap().eq(moon) {
            scrap_and_weights.push((
                row.get(2).unwrap().parse::<f64>().unwrap(),
                row.get(1).unwrap().parse::<f64>().unwrap(),
            ));
        }
    }
    scrap_and_weights
}

fn single_run(scrap_and_weights: &Vec<(f64, f64)>, scrap_amounts: u64) -> f64 {
    let mut scrap_for_run: Vec<f64> = Vec::new();

    /* I don't know how the fuck this works. It was in the docs */
    let dist = WeightedIndex::new(
        scrap_and_weights
            .iter()
            .map(|scrap_and_weights| scrap_and_weights.1),
    )
    .unwrap();

    /* Why the hell does this have to be mutable */
    let mut rng = thread_rng();
    for _ in 0..scrap_amounts {
        scrap_for_run.push(scrap_and_weights[dist.sample(&mut rng)].0);
    }
    let mut one_run_sum: f64 = 0.0;
    for scrap in scrap_for_run {
        one_run_sum += scrap;
    }
    one_run_sum
}

fn main() {
    /*
    filename gives the path to our csv file
    moon uses the first three characters of a moon's name to select it
    number_of_runs is how many simulated runs to use. 1 million seems to get very accurate
    */
    let filename: &str = "src/lethalcompany_scrap_table.csv";
    let moon: &str = "ass";
    let number_of_runs: u64 = 1_000_000;

    /* This returns the scrap values and their weights for the selected moon. Values are returned as floats inside tuples inside a vector. I swear this makes sense. */
    let scrap_and_weights = get_possible_scrap_weights(filename, moon);

    /* MeanSD uses its own type to run its mean and stdev calculations, so each run will be stored here */
    let mut total_scrap = MeanSD::default();

    /* This is where we actually preform the runs */
    for _ in 0..number_of_runs {
        /* Get the amount of scrap on the moon, runs a random number in the possible range */
        let scrap_amounts = get_scrap_amounts(moon);

        /* This returns the scrap from one run added together */
        let one_run = single_run(&scrap_and_weights, scrap_amounts);

        /* Adds scrap from one run to the type to later grab the mean and stdev */
        total_scrap.update(one_run);
    }

    /* Print all of the results */
    println!("Selected Moon: {}", moon);
    println!("Average Scrap Value: {}", total_scrap.mean());
    /* Whats the difference between population and sample stdev? I have no clue. They give similar results down to multiple decimal points */
    println!("Population StdDev: {}", total_scrap.pstdev());
    println!("Sample StdDev: {}", total_scrap.sstdev());
}
