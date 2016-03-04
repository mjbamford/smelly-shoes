class HomeController < ApplicationController

  def articles
    url = params[:url]
    @articles = Index.new(url).sniff
  end

  def article
  end
end
