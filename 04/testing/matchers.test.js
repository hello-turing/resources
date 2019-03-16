test('object assignment', () => {
    const data = {one: 1};
    data['two'] = 2;
    
    expect(data).toEqual(
        {
            one: 1,
            two: 2
        });
});

test('two plus two', () => {
    const value = 2 + 2;
    expect(value).toBeGreaterThan(3);
    expect(value).toBeGreaterThanOrEqual(3.5);
    expect(value).toBeLessThan(5);
    expect(value).toBeLessThanOrEqual(4.5);
  
    expect(value).toBe(4);
    expect(value).toEqual(4);
});