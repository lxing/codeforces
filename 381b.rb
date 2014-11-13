STDIN.gets
cards = STDIN.gets.strip.split.map {|x| x.to_i}
cards.sort!

stairs = []
leftovers = []
prev = 0

cards.each do |x|
  if x == prev
    leftovers << x  
  else
    stairs << x
  end
  prev = x
end

leftovers.reverse.each do |x|
  stairs << x unless x == prev
  prev = x
end

STDOUT.puts stairs.size
STDOUT.puts stairs.reverse.join(" ")
