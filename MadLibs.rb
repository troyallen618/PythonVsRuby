puts "Welcome to Troy's Mad Libs Adventure!"

puts "Enter a singular noun: "
A = gets.chomp
puts "Enter another singular noun: "
A2 = gets.chomp
puts"OK. This is the last singular noun you will have to input: "
A3 = gets.chomp
puts "Now, can you enter a plural noun: "
B = gets.chomp
puts "Please enter an adjective: "
C = gets.chomp
puts "One more adjective please: "
C2 = gets.chomp
puts "And another adjective: "
C3 = gets.chomp
puts "Enter Left or Right: "
D = gets.chomp.upcase

Left = "The "+A+ " turns the corner and sees another group of " + B + " and get captured.\nTHE END"
Right ="The "+A+ " runs into a " + C+" "+A2+" and a "+ C2+" "+A3+" who help fight off the "+B+". \nTHE END"


puts "One day a " + A + " was being chased by a group of " + C3 + " " + B + "."
puts'PRESS ENTER TO CONTINUE '
Z = gets
puts "The " + A + " ran to an intersection and decided to go " + D + "."
puts'PRESS ENTER TO CONTINUE '
Z = gets
if D == "LEFT"
	puts Left
else
	puts Right
end