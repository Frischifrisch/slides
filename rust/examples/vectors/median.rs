fn main() {
    let numbers = vec![10, 12, 11];
    println!("{:?}", numbers);
    println!("{}", median(&numbers));
    println!("{:?}", numbers);

    let numbers = vec![10, 12, 13, 11];
    println!("{:?}", numbers);
    println!("{}", median(&numbers));
    println!("{:?}", numbers);
}

fn median(numbers: &Vec<i32>) -> i32 {
    let mut numbers = numbers.clone();
    numbers.sort();
    let middle = numbers.len()/2;
    numbers[middle]
}
