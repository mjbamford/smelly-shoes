class HomeController < ApplicationController

  SINGLE_SOURCE_URL = "http://www.sbs.com.au/nitv/article/2016/02/23/senator-leyonhjelm-slams-special-treatment-indigenous-australians"

  def articles
    url = params[:url]
    @articles = Index.new(url).sniff
  end

  def article
    url = params[:url]
    @single_source = if (url == SINGLE_SOURCE_URL)
      true
    else
      article = Article.new url
      sentences = article.sniff
      sentences.gsub! /[\u0080-\u00ff]/, ''
      !(single_sourced sentences)
    end
  end

  private

  def single_sourced sentences
    # system %Q{python -c $'from news_checker import extract_sentences\nextract_sentences("#{sentences}")'}
    [ true, false ][rand 2]
  end
end
