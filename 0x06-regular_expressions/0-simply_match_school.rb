#!/usr/bin/env ruby

def match_school?(input)
  regex = /School/
  input =~ regex
end

if ARGV.length != 1
  puts "Usage: ruby script.rb <input>"
  exit 1
end

input = ARGV[0]

if match_school?(input)
  puts "#{input} matches the regular expression 'School'."
else
  puts "#{input} does not match the regular expression 'School'."
end
