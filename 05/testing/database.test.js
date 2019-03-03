const db = require("./database");

describe("Testing City Database", () => {
  beforeEach(() => {
    db.initializeDatabase();
  });

  afterEach(() => {
    db.clearDatabase();
  });

  it('should have Almaty city', () => {
    expect(db.isCity("Almaty")).toBeTruthy();
    db.deleteCity("Astana")
    db.printDatabase()
  })

  it('should have Astana city', () => {
    expect(db.isCity("Astana")).toBeTruthy();
  })
});
