// use std::fs::File;
// use std::io::{Error, Write};
use std::f64::consts::PI;

fn main() {

    // ===========================================================================================
    // This part here is for calculating the fiegenbaum constants by hand. It outputs a and d, and
    // you can collect those on your own to figure out what delta and alpha are.
    // ===========================================================================================
    // let a_next_guess = |a: f64, b: f64| -> f64 {a + (a - b)/(4.66)};

    // let n_period: u32 = 3;
    // let a0: f64 = 0.86;
    // let ap: f64 = 0.84;

    // let x0: f64 = 0.5;
    // let _dx0: f64 = 1.0;
    // let delta0: f64 = 1.0;
    
    // let e = f64::powf(10.0, -7.0);
    // let threshold = f64::powf(10.0, -15.0);
    // let max_steps = u64::pow(10, 10);

    // let a: f64 = newtons_loop(a0, x0, n_period, delta0, e, threshold, max_steps);

    // let d = f_peak(a, x0, i32::pow(2, n_period));

    // let a_next: f64 = a_next_guess(a, ap);

    // println!("a{} = {}", n_period, a);
    // println!("d{} = {}", n_period, d);
    // println!("a{} ~ {}", n_period + 1, a_next);

    // let a = delta(a_nnn, a_nn, a_n);
    // let d = delta(d_nnn, d_nn, d_n);

    // println!("delta = {}, alpha = {}", a, d);
    // println!("a{} = {}, a{} = {}, a{} = {}", n_input, a_n, n_input + 1, a_nn, n_input + 2, a_nnn);
    // println!("d{} = {}, d{} = {}, d{} = {}", n_input, d_n, n_input + 1, d_nn, n_input + 2, d_nnn);

    // ==============================================================================================
    // This part of the code allows a for loop to go over several values of a, guesses the next one,
    // and calculates the feigenbaum constants. It does everything. Also it's not perfect and doesn't
    // seem to like working on anything other then a loop that starts at n=2 with a=3.5
    // ==============================================================================================

    let feigenbaum_constant = |a: f64, b: f64, c: f64| -> f64 {(b - c)/(a - b)};

    let n_input: u32 = 1;
    let a_input: f64 = 3.3;
    let a_stable: f64 = 2.0;

    let f_steps: u32 = 8;

    let (a_vec, d_vec) = figenbaum_numbers(a_input, n_input, f_steps, a_stable);

    println!("###################\nSuper Stable Values\n#");
    for ii in 0..a_vec.len() {
        println!("\ta{} = {}\t\td{} = {}", ii + 1, a_vec[ii], ii + 1, d_vec[ii])
    }

    let i: usize = a_vec.len();

    println!("###################\nFigenbaum Constants\n#");
    for ii in 0..(i - 2){
        let de = feigenbaum_constant(a_vec[ii + 2], a_vec[ii + 1], a_vec[ii]);
        let al = feigenbaum_constant(d_vec[ii + 2], d_vec[ii + 1], d_vec[ii]);

        println!("\tFiegenbaum delta = {}\tFiegenbaum alpha = {}", de, al);

    }

}


fn fofax(a: f64, 
         x: f64) -> f64 {

    let return_x: f64 = a*x*(1.0 - x);

    return return_x;
}


fn dfofax(a: f64, 
          x: f64, 
          dx: f64) -> f64 {
    let return_dx: f64 = x*(1.0 - x) + a*(1.0 - 2.0*x)*dx;

    return return_dx
}


fn sofax(a: f64,
         x: f64) -> f64 {
    let return_x: f64 = a*(x*PI).sin();

    return return_x
         }


fn dsofax(a: f64,
          x: f64,
          dx: f64) -> f64 {
    let return_dx: f64 = (x*PI).sin() + a*(x*PI).cos()*dx;

    return return_dx
          }


fn newtons_loop(a0: f64, 
                x0: f64, 
                n_period: u32,
                delta0: f64,
                e: f64,
                threshold: f64,
                max_steps: u64) -> f64 {


    let mut a: f64 = a0;
    let mut aa: f64 = a0;
    let mut delta: f64 = delta0;
    if delta.abs() < threshold {

        println!("Function fails: threshold must be smaller then |delta|");

        return 0.0

    } else {

        let per = u64::pow(2, n_period);

        if per > 1000 {
            println!("This might take a while: period is over 1000")
        }

        for i in 1..=max_steps{

            // let mut jsteps: u64;

            let steps = i;

            let mut x: f64 = x0;
            // let mut dx: f64 = dx0;
            let mut dx: f64 = 1.0;
        
            for _j in 1..=per{

                // jsteps = j;

                let xx: f64 = fofax(a, x);
                let dxx: f64 = dfofax(a, x, dx);
                // let xx: f64 = sofax(a, x);
                // let dxx: f64 = dsofax(a, x, dx);
    
                x = xx;
                dx = dxx;

                // if j % 10000 == 0 {
                //     println!("j = {} ...", j)
                // }
    
            }

            let g: f64 = x - x0;
            let da: f64 = dx;
            delta = g/da;

            let c = e / (e + delta.abs());

            a = a - c * delta;

            if steps % 1000000 == 0 {
                // println!("Finished step {}, a currently at a = {}", steps, a);
                println!("i = {} ...", i);

                if aa == a {
                    println!("Pointless to continue, a hasn't changed");

                    break;
                }

                aa = a;
            }

            if delta.abs() < threshold {

                println!("finished in {} steps", steps);
        
                break;

            }
    
        }

        // println!("a = {}", a);
        println!("Finished");

        return a

    }

}


fn f_peak(a: f64, f0: f64, period: i32) -> f64 {
    let mut f: f64 = f0;

    for _k in 1..=period/2 {
        f = fofax(a, f);
        // f = sofax(a, f);
    }

    let displace: f64 = f - f0;

    return displace

}


// fn figenbaum_numbers_old(a_guess: f64, n_start: u32) -> ((f64, f64, f64), (f64, f64, f64)) {

//     let a_next_guess = |a: f64, b: f64| -> f64 {a + (a - b)/(4.0)};
//     let n_next = |n: u32| -> u32 {n + 1};
//     let _e_next = |n:f64| -> f64 {n - 1.0};

//     let a_n0 = if a_guess == 3.5 {3.0} else {a_guess};
//     let n: u32 = n_start;

//     let mut a_0: f64 = a_guess;

//     let x0: f64     = 0.5;
//     let _dx0: f64    = 1.0;
//     let _delta0: f64 = 1.0;

//     let en: f64   = -7.0;
//     let _enn: f64  = -8.0;
//     let _ennn: f64 = -9.0;
    
//     let threshold = f64::powf(10.0, -15.0);
//     let max_steps = u64::pow(10, 10);

//     let a_n: f64   = newtons_loop(a_0, x0, n,      1.0, f64::powf(10.0, en),       threshold, max_steps);
//     let d_n: f64 = f_peak(a_n, x0, i32::pow(2, n));
//     println!("a{} = {}, d{} = {}", n, a_n, n, d_n);
    
//     a_0 = a_next_guess(a_n, a_n0);
//     // let nn_start: u32 = n_start + 1;
//     let nn: u32 = n_next(n);
//     let a_nn: f64  = newtons_loop(a_0, x0, nn,  1.0, f64::powf(10.0, en - 2.0), threshold, max_steps);
//     let d_nn: f64 = f_peak(a_nn, x0, i32::pow(2, nn));
//     println!("a{} = {}, d{} = {}", nn, a_nn, nn, d_nn);

//     a_0 = a_next_guess(a_nn, a_n);
//     let nnn: u32 = n_next(nn);
//     let a_nnn: f64 = newtons_loop(a_0, x0, nnn, 1.0, f64::powf(10.0, en - 4.0), threshold, max_steps);
//     let d_nnn: f64 = f_peak(a_nnn, x0, i32::pow(2, nnn));
//     println!("a{} = {}, d{} = {}", nnn, a_nnn, nnn, d_nnn);

//     // let d: f64 = 0.0;

//     return ((a_n, a_nn, a_nnn), (d_n, d_nn, d_nnn))
// }


fn figenbaum_numbers(a_guess: f64, n_start: u32, steps: u32, a_start: f64) -> (Vec<f64>, Vec<f64>) {

    let a_next_guess = |a: f64, b: f64| -> f64 {a + (a - b)/(4.66)};
    let n_next = |n: u32| -> u32 {n + 1};
    let _e_next = |n:f64| -> f64 {n - 1.0};

    // let a_n0 = if a_guess == 3.5 {3.0} else {a_guess};
    let mut n: u32 = n_start;

    let mut a_0: f64 = a_guess;
    let mut a_p: f64 = a_start;

    let x0: f64 = 0.5;

    let en: f64 = -7.0;
    
    let threshold = f64::powf(10.0, -15.0);
    let max_steps = u64::pow(10, 10);

    // let mut a_n: f64 = 0.0;

    let mut a_vec: Vec<f64> = vec![];
    let mut d_vec: Vec<f64> = vec![];

    for _i in 1..=steps{

        let a_n: f64 = newtons_loop(a_0, x0, n, 1.0, f64::powf(10.0, en), threshold, max_steps);
        let d_n: f64 = f_peak(a_n, x0, i32::pow(2, n));

        a_vec.push(a_n);
        d_vec.push(d_n);

        a_0 = a_next_guess(a_n, a_p);
        a_p = a_n;
        n = n_next(n);

        println!("a_{} = {}, a_p = {}", n, a_0, a_p)
    }

    return (a_vec, d_vec)
}
