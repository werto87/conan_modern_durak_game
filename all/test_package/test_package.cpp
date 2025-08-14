#include <modern_durak_game/server/server.hxx>
#include <boost/json/src.hpp>
BOOST_FUSION_DEFINE_STRUCT ((test), Player, (std::string, playerId) )

int main() {
  [[maybe_unused]]auto server=modern_durak_game::Server{};

  return 0;
}
