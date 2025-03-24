countEvens :: [Int] -> Int
countEvens = length . filter even

main :: IO ()
main = print (countEvens [1, 2, 3, 4, 5, 6])