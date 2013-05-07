require 'spec_helper'

module Spatio
  describe Frontend do
    it 'should respnd to getItems' do
      Spatio::Frontend.should respond_to :getItems
    end
  end
end
