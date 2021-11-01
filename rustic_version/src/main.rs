fn main() {

    // let n_period: u32 = 1;
    // let a0: f64 = 3.1;

    // let x0: f64 = 0.5;
    // let _dx0: f64 = 1.0;
    // let delta0: f64 = 1.0;
    
    // let e = f64::powf(10.0, -7.0);
    // let threshold = f64::powf(10.0, -15.0);
    // let max_steps = u64::pow(10, 10);

    // let _a: f64 = newtons_loop(a0, x0, n_period, delta0, e, threshold, max_steps);

    let d: (f64, f64, f64, f64) = figenbaum_numbers(3.5, 2);
    // let (a, delta) = newtons_loop(3.55, 0.5, 3, 1.0, f64::powf(10.0, -7.0), f64::powf(10.0, -7.0), u64::pow(10, 10));
    // let d = f_peak(a, 0.5, i32::pow(2, 2));


    // let f_num: f64 = d.1;

    // println!("Found a = {}, delta = {}, d = {}", a, delta, d)
    println!("Found values of {:?}", d)

    // The automated process is not working, because it's very sensitive to inital conditions. Do it manually

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


fn newtons_loop(a0: f64, 
                x0: f64, 
                n_period: u32,
                delta0: f64,
                e: f64,
                threshold: f64,
                max_steps: u64) -> (f64, f64) {


    // let mut jsteps: u64 = 0;

    let mut a: f64 = a0;
    let mut aa: f64 = a0;
    let mut delta: f64 = delta0;
    if delta.abs() < threshold {

        println!("Function fails: threshold must be smaller then |delta|");

        return (0.0, 0.0)

    } else {

        let per = u64::pow(2, n_period);

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
    
                x = xx;
                dx = dxx;
    
            }

            let g: f64 = x - x0;
            let da: f64 = dx;
            delta = g/da;

            let c = e / (e + delta.abs());

            a = a - c * delta;

            if steps % 1000000 == 0 {
                println!("Finished step {}, a currently at a = {}", steps, a);

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

        println!("a = {}", a);

        return (a, delta)

    }

}


fn f_peak(a: f64, f0: f64, period: i32) -> f64 {
    let mut f: f64 = f0;

    for _k in 1..=period/2 {
        f = fofax(a, f);
    }

    let displace: f64 = f - f0;

    return displace

}


fn figenbaum_numbers(a_guess: f64, n_start: u32) -> (f64, f64, f64, f64) {
    // Run the newtons_loop over and over again. Want to do it x number of times. Or just do it in clusters?
    // Give an aN, yeild an a(N+1)
    // Use a(N+1) to find a(N+2)

    // Then find d = (a(N+1) - aN)/(a(N+2) - a(N+1))

    // let n_period: u32 = 1;
    // let a0: f64 = 3.1;

    // let exponent_neg: f64 = -2.0;
    // let exponent: f64 = 2.0;
    // let test_neg = f64::powf(2.0, exponent_neg);
    // let test = f64::powf(2.0, exponent);

    let a_next_guess = |a: f64, b: f64| -> f64 {a - (a - b)/(4.66)};

    let mut a_0: f64 = a_guess;

    let _adjust: f64 = 1.02;

    let x0: f64     = 0.5;
    let _dx0: f64    = 1.0;
    let _delta0: f64 = 1.0;

    let en: f64   = -7.0;
    let _enn: f64  = -8.0;
    let _ennn: f64 = -9.0;
    
    let threshold = f64::powf(10.0, -15.0);
    let max_steps = u64::pow(10, 10);

    let (a_n,   delta_n): (f64, f64)   = newtons_loop(a_0, x0, n_start,      1.0, f64::powf(10.0, en),       threshold, max_steps);
    
    a_0 = a_next_guess(a_n, a_0);
    println!("New a0 = {}", a_0);
    let (a_nn,  delta_nn): (f64, f64)  = newtons_loop(a_0, x0, n_start + 1,  1.0, f64::powf(10.0, en - 2.0), threshold, max_steps);

    a_0 = a_next_guess(a_nn, a_n);
    println!("New New a0 = {}", a_0);
    let (a_nnn, _delta_nnn): (f64, f64) = newtons_loop(a_0, x0, n_start + 2, 1.0, f64::powf(10.0, en - 4.0), threshold, max_steps);

    let d: f64 = (a_nn - a_n) / (a_nnn - a_nn); 

    // let d: f64 = 0.0;

    return (d, a_n, a_nn, a_nnn)
}