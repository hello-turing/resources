var cities = [];

const printDatabase = () => {
  console.log(cities);
};

const initializeDatabase = () => {
  cities = [
    {
      cityName: "Almaty",
      population: 1500000
    },
    {
      cityName: "Astana",
      population: 1000000
    },
    {
      cityName: "Karagandy",
      population: 600000
    }
  ];
};

const clearDatabase = () => {
  cities = [];
};

const isCity = cityName => {
  for (const city of cities) {
    if (city.cityName === cityName) {
      return true;
    }
  }
  return false;
};

const deleteCity = cityName => {
  cities = cities.filter(city => {
      return city.cityName != cityName
  })
};

module.exports = { printDatabase, initializeDatabase, clearDatabase, isCity, deleteCity };
