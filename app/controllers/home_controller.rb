class HomeController < ApplicationController

  def articles
    url = params[:url]
    @articles = Index.new(url).sniff
  end

  def sniff_articles
    urls = params[:articles].split(",")
    @sentences = urls.inject({}) do |memo, url|
      article = Article.new url
      sentences = article.sniff
      memo.merge({ url => sentences })
    end
  end
end
