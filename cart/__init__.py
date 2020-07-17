from .buy import buy


async def setup(bot):
    cog = buy()
    await cog.register_casetypes()
    bot.add_cog(cog)
