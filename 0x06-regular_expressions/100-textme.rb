#!/usr/bin/env ruby
# Using non-greedy way
puts ARGV[0].scan(/\[(?:from|to|flags):(.*?)\]/ix).join(',')
