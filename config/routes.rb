Rails.application.routes.draw do
  # For details on the DSL available within this file, see http://guides.rubyonrails.org/routing.html

  # Serve websocket cable requests in-process
  # mount ActionCable.server => '/cable'
  get '/sniff/article/:url' => 'home#article', as: 'article_sniffer'
  get '/sniff' => 'home#articles'
  root to: 'home#index'
end
