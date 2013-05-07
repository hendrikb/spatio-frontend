require 'sinatra'
require 'sinatra/reloader' if settings.environment == :development

set :root, File.dirname(__FILE__)
Dir.chdir settings.root

set :api_key, 'zghJGakaslknas'
enable :logging


######## move stuff below to external file structures ##########


get '/get_items/:ns/:lat/:lon/:range/:limit' do
  "Hello World"
end

