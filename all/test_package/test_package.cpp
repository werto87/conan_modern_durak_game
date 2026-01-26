#include <boost/json/src.hpp>
#include <modern_durak_game/server/server.hxx>

BOOST_FUSION_DEFINE_STRUCT((test), Player, (std::string, playerId))

int main() {

  boost::asio::io_context ioContext_{};
  boost::asio::ip::tcp::endpoint userToGameViaMatchmakingEndpoint_{};
  boost::asio::ip::tcp::endpoint matchmakingGameEndpoint_;
  [[maybe_unused]] auto server = modern_durak_game::Server{
      ioContext_, userToGameViaMatchmakingEndpoint_, matchmakingGameEndpoint_};

  return 0;
}
