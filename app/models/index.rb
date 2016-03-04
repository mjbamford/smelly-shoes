class Index
  require 'uri'
  require 'open-uri'

  SNIFF_TARGET = ".node-article a"

  attr_reader :doc

  def initialize url
    @url = url
    uri = URI url
    @domain = (uri.scheme || "http") + "://" + uri.host
  end

  def sniff
    @doc = Nokogiri::HTML open @url
    articles = doc.css SNIFF_TARGET
    articles.map { |a| @domain + a["href"] }.uniq
  end
end
