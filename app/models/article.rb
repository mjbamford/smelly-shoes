class Article
  require 'open-uri'

  SNIFF_TARGET = ".field-body p"

  def initialize url
    @url = url
  end

  def sniff
    doc = Nokogiri::HTML open @url
    doc.css SNIFF_TARGET
    doc.text
  end
end
