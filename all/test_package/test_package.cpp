#include <modern_durak_game/server/server.hxx>

BOOST_FUSION_DEFINE_STRUCT ((test), Player, (std::string, playerId) )

int main() {
  [[maybe_unused]]auto server=modern_durak_game::Server{};

  return 0;
}
