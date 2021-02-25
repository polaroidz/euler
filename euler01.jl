function solve()
    x = 0
    i = 1

    for i = 1:(1000 - 1)
        if i % 3 == 0 || i % 5 == 0
            x += i
        end
    end

    return x
end

ans = solve()
@time print(ans)
