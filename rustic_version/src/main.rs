fn main() {

    let n_period: u32 = 3;
    let a0: f64 = 3.6;

    let x0: f64 = 0.5;
    let _dx0: f64 = 1.0;
    let delta0: f64 = 1.0;
    
    let e = f64::powf(10.0, -7.0);
    let threshold = f64::powf(10.0, -15.0);
    let max_steps = u64::pow(10, 10);

    newtons_loop(a0, x0, n_period, delta0, e, threshold, max_steps)

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
                max_steps: u64) {


    let mut a: f64 = a0;
    let mut aa: f64 = a0;
    let mut delta: f64 = delta0;
    if delta.abs() < threshold {

        println!("Function fails: threshold must be smaller then |delta|")

    } else {

        let per = u64::pow(2, n_period);

        for i in 1..=max_steps{

            let steps = i;

            let mut x: f64 = x0;
            // let mut dx: f64 = dx0;
            let mut dx: f64 = 1.0;
        
            for _j in 1..=per{

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

        println!("a = {}", a)

    }

}