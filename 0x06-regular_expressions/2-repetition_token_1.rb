#!/usr/bin/env ruby

def match_school?(input)
  regex = /\bSchool\b/i  # Case-insensitive match for the whole word
  !!(input =~ regex)
end

if ARGV.length != 1
  puts "Usage: ruby script.rb <input>"
  exit 1
end

input = ARGV[0]

if match_school?(input)
  puts "#{input} contains the word 'School'."
else
  puts "#{input} does not contain the word 'School'."
end
