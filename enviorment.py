import gym


class TradingEnv(gym.Env):
    def __init__(self, train_data, init_capital):
        self.stock_return_rate_history = train_data
        self.n_stocks = train_data.shape[1]
        self.n_steps = train_data.shape[0]

        self.init_capital = init_capital
        self.current_step = None
        self.stock_owned = None
        self.stock_return_rate = None
        self.current_capital = None

        #5 options, 0%, 25%, 50%, 75% or 100% for each stock
        self.action_space = spaces.Discrete(5**self.n_stock)
        #observation space is set
        self.observation_space = spaces.MultiDiscrete(5**self.n_stock + init_capital*2)


    
