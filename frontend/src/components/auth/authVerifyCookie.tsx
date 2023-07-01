import nookies from 'nookies'
import absoluteUrl from 'next-absolute-url'
import fetch from 'isomorphic-unfetch'
import type { NextPageContext } from 'next'
import { TrendingUp } from 'react-feather'

const authVerifyCookie = async (ctx: NextPageContext) => {

	// Get cookies from context
	const cookies = nookies.get(ctx)
	
	// Get absolute origin url
	const { origin } = absoluteUrl(ctx.req)

	// Try to verify user token via API
	// return await fetch(origin + '/api/auth', {
	// 	method: 'POST',
	// 	headers: {
	// 		'Content-Type': 'application/json',
	// 	},
	// 	body: JSON.stringify({ token: cookies.buc_token }),
	// }).then((res: fetch.IsomorphicResponse) => {
	// 	if (res.ok) {
	// 		return res.json()
	// 	} else {
	// 		return false
	// 	}
	// })
	return true;
}

export default authVerifyCookie
