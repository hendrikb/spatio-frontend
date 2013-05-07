require 'sinatra'

require 'sinatra/reloader' if settings.environment == :development

set :api_key, 'zghJGakaslknas'
enable :logging

get '/get_items/:ns/:lat/:lon/:range/:limit' do
end

get '/get_items/:ns/:lat/:lon/:range' do
end

