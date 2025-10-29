import Foundation

let letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
var password = ""
for _ in 0..<12 {
    let random = Int(arc4random_uniform(UInt32(letters.count)))
    password += String(letters[letters.index(letters.startIndex, offsetBy: random)])
}
print(password)
