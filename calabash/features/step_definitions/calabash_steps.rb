require 'calabash-android/calabash_steps'

When(/^I press key (\d+)$/) do |arg1|
  performAction("press_key", 7+arg1.to_i)
end

When(/^I enter "([^"]*)"$/) do |arg1|
  arg1.split("").each do |i|
    performAction("press_key", 7+i.to_i)
  end
end

When(/^I touch Prev/) do ||
  touch("AppCompatButton id:'btnPrev'")
end

When(/^I touch Done/) do ||
  touch("AppCompatButton id:'btnDone'")
end

Then(/^I check button Prev disabled$/) do
  check_element_exists("AppCompatButton id:'btnPrev' enabled:'false'")
end

Then(/^I check button Prev enabled$/) do
  check_element_exists("AppCompatButton id:'btnPrev' enabled:'true'")
end

Then(/^I check button Next disabled$/) do
  check_element_exists("AppCompatButton id:'btnNext' enabled:'false'")
end

Then(/^I check button Next enabled$/) do
  check_element_exists("AppCompatButton id:'btnNext' enabled:'true'")
end

Then(/^I check button Done disabled$/) do
  check_element_exists("AppCompatButton id:'btnDone' enabled:'false'")
end

Then(/^I check button Done enabled$/) do
  check_element_exists("AppCompatButton id:'btnDone' enabled:'true'")
end

Then(/^I see icon unknown$/) do
  check_element_exists("CreditEditText contentDescription:'unknown'")
end

Then(/^I see icon mastercardfront$/) do
  check_element_exists("CreditEditText contentDescription:'mastercardfront'")
end

Then(/^I see icon visafront$/) do
  check_element_exists("CreditEditText contentDescription:'visafront'")
end

When(/^I wait (\d+) sec$/) do |arg1|
  sleep(arg1.to_i)
end

Given(/^payment server$/) do
  r=`${PROJECT_ROOT}/restart.sh`
  puts r
end

Then(/^I find db entry$/) do
  doc_id = `curl -s http://localhost:5985/payments/_all_docs | grep -Po '"id":.*?[^\\\\]",' | perl -pe 's/"id"://; s/^"//; s/",$//'`
  puts "Found document with id=#{doc_id}"
  doc_entry = `curl -s http://localhost:5985/payments/#{doc_id}`
  puts "Found document entry '#{doc_entry}'"
  r=`echo '#{doc_entry}' | grep -P '"type".?:"user"'`
  if r.empty?
    fail("Payment not found in db")
  end
  puts "Found field #{r}"
end
