class HomeController < ApplicationController

  def articles
    url = params[:url]
    @articles = Index.new(url).sniff
  end

  def article
    url = params[:url]
    article = Article.new url
    sentences = article.sniff
    sentences.gsub! /[\u0080-\u00ff]/, ''
    # @single_source = [ true, false ][rand 2]
    @single_source = !(single_sourced sentences)
  end

  private

  def single_sourced sentences
    system %Q{python -c $'from news_checker import extract_sentences\nextract_sentences("#{sentences}")'}
  end
end
